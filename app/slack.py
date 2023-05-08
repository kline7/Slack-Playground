import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.models.channels import Channels
from typing import Optional

logging.basicConfig(level=logging.DEBUG)


slack_token = os.environ["API_TOKEN_KEY"]


class SlackBot:
    def __init__(self, token):
        self.token = token
        self._client = WebClient(token=token)

    def post_message(
        self,
        channel: str,
        message: str,
        post_at: Optional[int] = None
    ):
        try:
            if post_at:
                response = self._client.chat_scheduleMessage(
                    channel=channel,
                    text=message,
                    post_at=post_at
                )
            else:
                response = self._client.chat_postMessage(
                    channel=channel,
                    text=message
                )
        except SlackApiError as e:
            assert e.response["error"]
        return response

    def list_channels(self) -> Channels:
        try:
            response = self._client.conversations_list()
            response = Channels(**response.__dict__["_initial_data"])
        except SlackApiError as e:
            assert e.response["error"]
        return response


slack_bot = SlackBot(slack_token)
