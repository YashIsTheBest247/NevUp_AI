import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from backend.database import Base, engine
from backend.seed import seed_data
from backend.routes import trades, metrics

app = FastAPI()

# ✅ Wait for DB to be ready
def wait_for_db():
    retries = 10
    while retries > 0:
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected!")
            return
        except OperationalError:
            print("⏳ Waiting for database...")
            time.sleep(3)
            retries -= 1
    raise Exception("❌ Database not ready after retries")

@app.on_event("startup")
def startup():
    wait_for_db()
    seed_data()

app.include_router(trades.router)
app.include_router(metrics.router)