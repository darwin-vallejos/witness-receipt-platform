# WRP-1 CANONICALIZATION — FROZEN
# Do not modify. Any change requires WRP-2.
#
# This file defines the canonical JSON rules for the
# Witness Receipt Protocol version 1 (WRP-1).
#
# Canonicalization rules are immutable for WRP-1.

import json
from typing import Dict, Any


def canonicalize(payload: Dict[str, Any]) -> str:
    """
    WRP-1 Canonical JSON Rules:

    - UTF-8 encoding
    - JSON objects sorted by key (lexicographically)
    - No insignificant whitespace
    - Arrays preserved in order
    - Deterministic number serialization
    - No semantic interpretation

    The returned string is the canonical representation
    used for SHA-256 hashing.
    """

    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
