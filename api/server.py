from fastapi import FastAPI, UploadFile, File
from storage.store import init_db, store_receipt
import hashlib

PRIMITIVE_VERSION = "v1.2-final"

app = FastAPI(title="BIP-2 Platform")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    return {"status": "ok", "service": "bip2-platform", "boundary": "primitive-external"}


@app.get("/about")
def about():
    return {
        "name": "bip2-platform",
        "role": "convenience-wrapper",
        "authority": "none",
        "primitive": f"bip2-primitive {PRIMITIVE_VERSION}",
        "guarantees": [
            "does not modify primitive behavior",
            "does not interpret hashes",
            "does not validate correctness",
        ],
    }


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    data = await file.read()
    digest = hashlib.sha256(data).hexdigest()

    receipt_id = store_receipt(
        hash_result=digest,
        byte_count=len(data),
        primitive_version=PRIMITIVE_VERSION,
    )

    return {
        "storage_id": receipt_id,
        "hash_result": digest,
        "byte_count": len(data),
        "primitive_version": PRIMITIVE_VERSION,
        "note": "persisted neutral receipt (no interpretation)",
    }
