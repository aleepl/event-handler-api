from fastapi import APIRouter, Depends
from utils.slack_tools import Slack
from models.slack_event import SlackEventRequest
from core.dependencies import validate_api_key
from core.config import config
from utils.custom_logging import log_msg

router = APIRouter()


@log_msg("Call to /slack/events endpoint", slack_log=True, add_breakline=False)
@router.post("/events")
async def handle_slack_event(request: SlackEventRequest, api_key: str = Depends(validate_api_key)):
    """Endpoint for Slack Events API."""
    # Handle Slack URL verification challenge
    if request.type == "url_verification":
        return {"challenge": request.challenge}

    # Process file_shared events
    if request.event and request.event.get("type") == "file_shared":
        file_id = request.event.get("file_id")
        Slack(config.slack_app_token).download_file(file_id, config.slack_event_target)

    # Send signal to pipelines using these events
    return {"status": "ok"}
