###############
Message to Slack Service
###############

Rate Limiting:
* Slack allows applications to send no more than one message per channel per second.
* However, they do allow bursts over that limit for a short period of time.
* Rate limiting results in a 429 response

```python
import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

# Simple wrapper for sending a Slack message
def send_slack_message(channel, message):
    return client.chat_postMessage(
        channel=channel,
        text=message
    )

# Make the API call and save results to `response`
channel = "#random"
message = "Hello, from Python!"
# Do until being rate limited
while True:
    try:
        response = send_slack_message(channel, message)
    except SlackApiError as e:
        if e.response.status_code == 429:
            # The `Retry-After` header will tell you how long to wait before retrying
            delay = int(e.response.headers['Retry-After'])
            print(f"Rate limited. Retrying in {delay} seconds")
            time.sleep(delay)
            response = send_slack_message(channel, message)
        else:
            # other errors
            raise e
```

However, there are better error handling docs here(https://api.slack.com/docs/rate-limits)

