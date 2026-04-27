from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.metrics import Metrics
from backend.services.auth import verify_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/{user_id}/metrics")
def get_metrics(user_id: str, payload=Depends(verify_token), db: Session = Depends(get_db)):

    if payload["sub"] != user_id:
        raise HTTPException(403, "Cross-tenant access denied")

    return db.query(Metrics).filter_by(userId=user_id).all()