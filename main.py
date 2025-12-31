"""
Witness Receipt Protocol — WRP-1
STATUS: FROZEN

This implementation MUST NOT change canonicalization or hashing behavior.
Any modification requires a new schema_version.

© Darwin Vallejos
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import hashlib
import json
import sqlite3
import uuid
from datetime import datetime

# ============================================================
# App
# ============================================================

app = FastAPI(
    title="WRP Platform",
    version="WRP-1",
    description="Deterministic receipt issuance and verification (Canonical JSON + SHA-256)",
)

# ============================================================
# Database (storage only, not part of verification)
# ============================================================

DB_FILE = "receipts.db"


def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS receipts (
            receipt_id TEXT PRIMARY KEY,
            schema_version TEXT NOT NULL,
            receipt_hash TEXT NOT NULL,
            canonical TEXT NOT NULL,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()

# ============================================================
# Canonicalization & Hashing (LOCKED — DO NOT CHANGE)
# ============================================================


def canonicalize(payload: Dict[str, Any]) -> str:
    """
    Canonical JSON rules:
    - sort_keys = True
    - separators = (",", ":")
    - ensure_ascii = False
    - UTF-8 encoding
    """
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def compute_hash(payload: Dict[str, Any]) -> str:
    canonical = canonicalize(payload)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ============================================================
# Models (PURE WRP — NO BUSINESS FIELDS)
# ============================================================

class ReceiptCreateRequest(BaseModel):
    payload: Dict[str, Any]


class ReceiptCreateResponse(BaseModel):
    schema_version: str
    receipt_id: str
    receipt_hash: str
    canonical: str
    payload: Dict[str, Any]
    created_at: str


class ReceiptVerifyRequest(BaseModel):
    payload: Dict[str, Any]
    receipt_hash: str


class ReceiptVerifyResponse(BaseModel):
    valid: bool
    computed_hash: str


# ============================================================
# Routes
# ============================================================

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/receipt/create", response_model=ReceiptCreateResponse)
def create_receipt(req: ReceiptCreateRequest):
    payload = req.payload

    canonical = canonicalize(payload)
    receipt_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    receipt_id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat() + "Z"

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO receipts (
            receipt_id,
            schema_version,
            receipt_hash,
            canonical,
            payload,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            receipt_id,
            "WRP-1",
            receipt_hash,
            canonical,
            json.dumps(payload, separators=(",", ":"), ensure_ascii=False),
            created_at,
        ),
    )
    conn.commit()
    conn.close()

    return {
        "schema_version": "WRP-1",
        "receipt_id": receipt_id,
        "receipt_hash": receipt_hash,
        "canonical": canonical,
        "payload": payload,
        "created_at": created_at,
    }


@app.post("/api/receipt/verify", response_model=ReceiptVerifyResponse)
def verify_receipt(req: ReceiptVerifyRequest):
    canonical = canonicalize(req.payload)
    computed_hash = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    return {
        "valid": computed_hash == req.receipt_hash,
        "computed_hash": computed_hash,
    }
