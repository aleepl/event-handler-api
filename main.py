from fastapi import FastAPI
from routers import slack

app = FastAPI()

app.include_router(slack.router, prefix="/slack", tags=["Slack"])
