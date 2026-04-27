from backend.database import SessionLocal
from backend.models.trade import Trade
from backend.models.metrics import Metrics
from dateutil.parser import parse
import json, uuid

def compute_metrics(trade_id):
    db = SessionLocal()

    trade = db.query(Trade).filter_by(tradeId=trade_id).first()
    if not trade:
        return

    trades = db.query(Trade)\
        .filter(Trade.userId == trade.userId)\
        .order_by(Trade.entryAt.asc())\
        .all()

    # 1 Plan adherence
    last_10 = trades[-10:]
    avg_plan = sum([(t.planAdherence or 0) for t in last_10]) / len(last_10)

    # 2 Revenge trade
    if len(trades) > 1:
        prev = trades[-2]
        if prev.outcome == "loss":
            delta = (parse(trade.entryAt) - parse(prev.exitAt)).seconds
            if delta <= 90 and trade.emotionalState in ["anxious", "fearful"]:
                trade.revengeFlag = "true"

    # 3 Session tilt
    session_trades = [t for t in trades if t.sessionId == trade.sessionId]
    loss_follow = sum(
        1 for i in range(1, len(session_trades))
        if session_trades[i-1].outcome == "loss"
    )
    tilt = loss_follow / len(session_trades) if session_trades else 0

    # 4 Emotion stats
    stats = {}
    for t in trades:
        if t.emotionalState:
            stats.setdefault(t.emotionalState, {"win": 0, "loss": 0})
            stats[t.emotionalState][t.outcome] += 1

    # 5 Overtrading
    window = [
        t for t in trades
        if abs((parse(trade.entryAt) - parse(t.entryAt)).seconds) <= 1800
    ]
    if len(window) > 10:
        print("⚠️ OVERTRADING EVENT")

    metric = Metrics(
        id=str(uuid.uuid4()),
        userId=trade.userId,
        planAdherenceAvg=avg_plan,
        tiltIndex=tilt,
        emotionStats=json.dumps(stats)
    )

    db.add(metric)
    db.commit()
    db.close()