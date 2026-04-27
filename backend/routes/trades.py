from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.trade import Trade
from backend.services.auth import verify_token
from backend.workers.worker import process_trade_task

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/trades")
def create_trade(trade: dict, payload=Depends(verify_token), db: Session = Depends(get_db)):

    if payload["sub"] != trade["userId"]:
        raise HTTPException(403, "Cross-tenant access denied")

    existing = db.query(Trade).filter_by(tradeId=trade["tradeId"]).first()
    if existing:
        return existing

    db.add(Trade(**trade))
    db.commit()

    process_trade_task.delay(trade["tradeId"])

    return {"status": "created"}