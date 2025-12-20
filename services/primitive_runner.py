import subprocess
from pathlib import Path

BIP2_BINARY = "bip2"  # frozen external primitive

def hash_file(path: Path) -> str:
    result = subprocess.run(
        [BIP2_BINARY, "hash", str(path)],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()
