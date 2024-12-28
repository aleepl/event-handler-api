from pydantic import BaseModel
from typing import Optional, Dict


class SlackEventRequest(BaseModel):
    type: str
    challenge: Optional[str] = None
    event: Optional[Dict] = {}
