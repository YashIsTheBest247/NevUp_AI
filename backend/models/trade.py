from sqlalchemy import Column, String, Float, Integer
from backend.database import Base

class Trade(Base):
    __tablename__ = "trades"

    tradeId = Column(String, primary_key=True)
    userId = Column(String)
    sessionId = Column(String)

    asset = Column(String)
    assetClass = Column(String)
    direction = Column(String)

    entryPrice = Column(Float)
    exitPrice = Column(Float, nullable=True)
    quantity = Column(Float)

    entryAt = Column(String)
    exitAt = Column(String, nullable=True)

    status = Column(String)
    outcome = Column(String)
    pnl = Column(Float)

    planAdherence = Column(Integer)
    emotionalState = Column(String)

    revengeFlag = Column(String, default="false")