from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime, timezone
import uuid

DATABASE_URL = "sqlite:///./storage/receipts.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(String, primary_key=True, index=True)
    hash_result = Column(String, nullable=False)
    byte_count = Column(Integer, nullable=False)
    primitive_version = Column(String, nullable=False)
    platform_timestamp = Column(DateTime, nullable=False)


def init_db():
    Base.metadata.create_all(bind=engine)


def store_receipt(hash_result: str, byte_count: int, primitive_version: str) -> str:
    db = SessionLocal()
    try:
        receipt_id = f"rec-{uuid.uuid4().hex}"
        receipt = Receipt(
            id=receipt_id,
            hash_result=hash_result,
            byte_count=byte_count,
            primitive_version=primitive_version,
            platform_timestamp=datetime.now(timezone.utc),
        )
        db.add(receipt)
        db.commit()
        return receipt_id
    finally:
        db.close()
