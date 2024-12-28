import os
import json
from datetime import datetime


class Config:
    # Current timestamp parameters
    timenow = datetime.now()
    executation_day = timenow.strftime("%Y%m%d")
    execution_time = timenow.strftime("%Hh%Mm%Ss")
    # Authentication
    allowed_api_key: dict = json.loads(os.environ.get("ALLOWED_API_KEY"))
    # Slack
    slack_app_token: str = os.environ.get("SLACK_OAUTH_TOKEN")
    slack_success_channel: str = os.environ.get("SLACK_SUCCESS_CHANNEL")
    slack_error_channel: str = os.environ.get("SLACK_ERROR_CHANNEL")
    # Configurations
    slack_event_target: str = os.environ.get("SLACK_EVENT_DATA")
    logging_target: str = os.environ.get("LOGGING_PATH")


config = Config()

if __name__ == "__main__":
    print(config.timenow)
    print(config.executation_day)
    print(config.execution_time)
    print(config.allowed_api_key)
    print(type(config.allowed_api_key))
    print(config.slack_app_token)
    print(config.slack_success_channel)
    print(config.slack_error_channel)
    print(config.slack_event_target)
    print(config.logging_target)
