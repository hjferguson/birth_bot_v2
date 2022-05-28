#Harlan Ferguson 2022-05-22
#Program that takes list of friends and texts them on their birthdays
#for details see README.txt
import datetime, smtplib, credentials as cred
from functions import convertCarrier as cc
now = datetime.datetime.now()
currentDate = now.strftime('%m-%d') #gets current month and day in format of .txt file
birthdays = {} #initialize dictionary.
subject = "Subject: HAPPY BIRTHDAY!" #for textmessage formatting
message = "\nHappy birthday! \nBest wishes,\nHarlan"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(cred.username, cred.password) #all text messages will be sent from this email address.

with open('birthdays.txt') as f:
    for line in f:
        (key, value) = line.split()
        birthdays[key] = value #converts .txt line to dictionary
#dictionary has phonenumber as key, and a string conisting of name=birthday=carrier as the value

for phoneNumber in birthdays:
    contact = birthdays[phoneNumber].split('=') #split creates a list, diff item every '='. 
    #contact[0] = name, contact[1] = birthday, contact[2] = carrier
    if currentDate == contact[1]:
        smsGateway = cc(contact[2]) #converts .txt format to SMS gateway format using function. works with Canadian providers
        server.sendmail(cred.username, f"{phoneNumber}@{smsGateway}", f"{subject} \nHi {contact[0]}, {message}")
        server.quit()
