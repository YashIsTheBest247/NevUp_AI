import pandas as pd
from backend.database import SessionLocal
from backend.models.trade import Trade

def seed_data():
    db = SessionLocal()

    try:
        # ✅ Prevent duplicate seeding
        if db.query(Trade).first():
            print("✅ Seed already exists, skipping...")
            return

        print("🌱 Seeding database...")

        df = pd.read_csv("data/nevup_seed_dataset.csv")

        # ✅ Get valid columns from model
        valid_columns = set(Trade.__table__.columns.keys())

        for _, row in df.iterrows():
            raw_data = row.to_dict()

            # ✅ Filter only valid columns + clean NaN
            cleaned_data = {
                key: (None if pd.isna(value) else value)
                for key, value in raw_data.items()
                if key in valid_columns
            }

            db.add(Trade(**cleaned_data))

        db.commit()
        print("✅ Seeding completed successfully!")

    except Exception as e:
        db.rollback()
        print("❌ Seeding failed:", str(e))
        raise e

    finally:
        db.close()