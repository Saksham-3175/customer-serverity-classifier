import json
from pathlib import Path
from datetime import datetime, timedelta
import os
from core.utils import DATA_DIR

DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_cache(name: str, data: dict, ttl_minutes: int = 30):
    path = DATA_DIR / f"{name}.json"
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "data": data,
        "_metadata": {"ttl_minutes": ttl_minutes},
    }
    try:
        path.write_text(json.dumps(payload, indent=2))
    except Exception:
        pass


def load_cache(name: str, ttl_minutes: int = 30):
    path = DATA_DIR / f"{name}.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text())
        ts = datetime.fromisoformat(payload.get("timestamp"))
        if datetime.utcnow() - ts > timedelta(minutes=ttl_minutes):
            return None
        return payload.get("data")
    except Exception:
        return None


def clear_cache(name: str):
    path = DATA_DIR / f"{name}.json"
    if path.exists():
        path.unlink()
