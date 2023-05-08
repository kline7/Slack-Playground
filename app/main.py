from datetime import datetime, timedelta
from app.slack import slack_bot

# Schedule a message
ct = datetime.now()
nt = ct + timedelta(minutes=1)
channels = slack_bot.list_channels()
general_channel = next(filter(lambda x: x.name == "general", channels.channels), None)
slack_bot.post_message(
    channel=general_channel.id,
    message="Senior Grubby is recieving his scheduled remainder to clean his stinky",
    post_at=nt.timestamp
)
