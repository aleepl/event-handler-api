from fastapi import Query, HTTPException
from core.config import config


def validate_api_key(api_key: str = Query(...)):
    """Dependency to validate API keys."""
    if api_key not in config.allowed_api_key.values():
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key
