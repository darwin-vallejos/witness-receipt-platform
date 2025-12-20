from fastapi import FastAPI, UploadFile, File
from datetime import datetime
from uuid import uuid4
import hashlib

app = FastAPI(title="BIP-2 Platform")

# -----------------------------
# ROOT: sanity ping
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "bip2-platform",
        "boundary": "primitive-external"
    }

# -----------------------------
# ABOUT: boundary contract
# -----------------------------
@app.get("/about")
def about():
    return {
        "name": "bip2-platform",
        "role": "convenience-wrapper",
        "authority": "none",
        "primitive": "bip2-primitive v1.2-final",
        "guarantees": [
            "does not modify primitive behavior",
            "does not interpret hashes",
            "does not add semantic meaning",
            "does not validate correctness"
        ]
    }

# -----------------------------
# EXPERIMENT #3: Neutral Pipeline (UPLOAD -> HASH -> RECEIPT)
# -----------------------------
@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()

    # PLATFORM-SAFE STUB:
    # Deterministic math, no semantics, no validation.
    digest = hashlib.sha256(data).hexdigest()

    return {
        "storage_id": f"rec-{uuid4().hex[:8]}",
        "hash_result": digest,
        "platform_timestamp": datetime.utcnow().isoformat() + "Z",
        "byte_count": len(data),
        "primitive_version": "v1.2-final",
        "note": "platform-safe sha256 stub (replace with frozen primitive call later)"
    }
