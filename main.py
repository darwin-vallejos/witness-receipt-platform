from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import hashlib
import json
import sqlite3
import uuid
from datetime import datetime

# -----------------------------
# App
# -----------------------------
app = FastAPI(
    title="Witness Receipt Platform",
    version="1.0.0",
    description="Deterministic receipts (WCJ-1 + SHA-256). v1.0 is hash-only."
)

# -----------------------------
# Database
# -----------------------------
DB_FILE = "receipts.db"

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            receipt_id TEXT PRIMARY KEY,
            schema_version TEXT NOT NULL,
            receipt_hash TEXT NOT NULL,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Canonical JSON (WCJ-1)
# -----------------------------
def canonicalize(payload: Dict[str, Any]) -> str:
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    )

def compute_hash(payload: Dict[str, Any]) -> str:
    canonical = canonicalize(payload)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()

# -----------------------------
# Models
# -----------------------------
class Payload(BaseModel):
    decision: str
    trust_score_bp: int
    amount_cents: int

class ReceiptRequest(BaseModel):
    payload: Payload

class ReceiptResponse(BaseModel):
    schema_version: str
    receipt_id: str
    receipt_hash: str
    created_at: str

# -----------------------------
# Routes
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/receipt/create", response_model=ReceiptResponse)
def create_receipt(req: ReceiptRequest):
    payload_dict = req.payload.dict()

    receipt_hash = compute_hash(payload_dict)
    receipt_id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat() + "Z"

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO receipts
        (receipt_id, schema_version, receipt_hash, payload, created_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            receipt_id,
            "1.0.0",
            receipt_hash,
            json.dumps(payload_dict),
            created_at
        )
    )
    conn.commit()
    conn.close()

    return {
        "schema_version": "1.0.0",
        "receipt_id": receipt_id,
        "receipt_hash": receipt_hash,
        "created_at": created_at
    }
