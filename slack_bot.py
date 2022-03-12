# Run this script only after exposing port 3000 with ngrok: ./ngrok htttp 3000
# You need to have ngrok installed and an account created to get an authtoken
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')

print('Using token: ' + SLACK_BOT_TOKEN)
print('Using secret: ' + SLACK_SIGNING_SECRET)

# Initializes your app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

# Add functionality here
@app.event("app_mention")
def reply(event, say):
    try:
        text = event['text']
        channel = event['channel']
        say(text=text, channel=channel)

        if '?' in text[-1]:
            say(text=text, channel=channel)
    except Exception as e:
        say("Something went wrong...")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
