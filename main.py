#Written by: Harlan Ferguson
#Program designed to be run on a raspberry pi and activated with cron jobs
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = client.messages.create(
    body="deez nuts",
    from_=TWILIO_PHONE_NUMBER,
    to="+16477039139"
)

print(message.sid)