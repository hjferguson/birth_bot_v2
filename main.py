#Written by: Harlan Ferguson
#Program designed to be run on a raspberry pi and activated with cron jobs
import os
import datetime
import pandas as pd
from dotenv import load_dotenv
from twilio.rest import Client

#get credentials
load_dotenv()
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

#get current month and day
current_date = datetime.datetime.now().date()
current_month = current_date.month
current_day = current_date.day

#make a df from csv
df = pd.read_csv('birthdays.csv')

#make a df of today's birthdays
todays_birthday = df[(df['month'] == current_month) & (df['day'] == current_day)]

if not todays_birthday.empty:
    for index, row in todays_birthday.iterrows():
        print(f"It's {row['name']}'s birthday! Sending a message to {row['cell_number']}")
        #make client object from the twilio API
        client = Client(ACCOUNT_SID,AUTH_TOKEN)
        message = client.messages.create(
            body= (f"🎂Happy Birthday, {row['name']}!!!🎂\n\nI hope you have a great day!\n\n-Harlan \nps. this is a bot, don't respond, I won't see it 😂"),
            from_=TWILIO_PHONE_NUMBER,
            to={row['cell_number']}
)
