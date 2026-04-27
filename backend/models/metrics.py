from sqlalchemy import Column, String, Float
from backend.database import Base

class Metrics(Base):
    __tablename__ = "metrics"

    id = Column(String, primary_key=True)
    userId = Column(String)

    planAdherenceAvg = Column(Float)
    tiltIndex = Column(Float)

    emotionStats = Column(String)