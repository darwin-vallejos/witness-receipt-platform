from fastapi import FastAPI, Request
import hashlib

app = FastAPI(title="BIP-2 Platform")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "bip2-platform",
        "boundary": "primitive-external"
    }

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

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.body()

    # TEMPORARY STUB (platform-safe)
    # This will later be replaced by an external call to bip2-primitive
    digest = hashlib.sha256(data).hexdigest()

    return {
        "bytes_received": len(data),
        "hash": digest,
        "source": "platform-wrapper"
    }
