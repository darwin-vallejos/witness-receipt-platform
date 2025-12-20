from pathlib import Path
from datetime import datetime
import shutil
from fastapi import UploadFile

STORAGE_ROOT = Path("storage/data")
STORAGE_ROOT.mkdir(parents=True, exist_ok=True)

def store_file(file: UploadFile):
    timestamp = datetime.utcnow().isoformat()
    destination = STORAGE_ROOT / file.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    metadata = {
        "filename": file.filename,
        "stored_at": timestamp
    }

    return destination, metadata
