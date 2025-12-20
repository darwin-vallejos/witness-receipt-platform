from fastapi import FastAPI

app = FastAPI(title="BIP-2 Platform")

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "bip2-platform",
        "boundary": "primitive-external"
    }
