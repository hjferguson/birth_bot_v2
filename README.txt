Welcome to the birthday_bot documentation! Written by Harlan Ferguson on May 22nd, 2022.
This program uses a spare email address to email-to-sms friends in the birthdays.txt database (db).
This project was done FOR FUN.

The db has a format of 'phonenumber name=month-day=carrier'. the space between the 'phonenumber' and 'name' 
allow for the program to convert the db to a dictionary. From there, the values are split from the '=' and can 
be accessed with contact[indexnumber]. It currently has 16 lines (friends) and if keeping same format, will dynamically work with
program.py. Uses phonenumber as the key since those are individual assignments and allow for multiple friends with same birthdays.

The spare email has 2-factor authentification and a special app password that you get through the security settings
this allows 3rd party apps (this program) to sign into a google account without google blocking the action. 

I am using a secondary program called credentials.py (git version requires your own credentials) to store my information so you could do the same, or directly add to the program.py.

I've tested the program on a few people in the list and an email text is sent to the direct message center of the recipient
however, wind/freedom users don't have this natively and need to text 'emailname@email.com Howdy' to '4000' in order to be able to 
recieve emails in future. So, any freedom users need to set this up before the bot works with them. Not sure if there is a cost. ¯\_(ツ)_/¯

How to find carriers? carrierlookup.com. 1 free lookup a day which can be exploited by using tor network. Requires recaptcha regardless
and takes about,30 seconds per lookup. So if this project gets bigger, will need paid API or different messaging method. 
Additionally, you could just ask... For 16 friends this is light work, but if this project ever made it to V2, this is an awful solution. 
This is needed because each carrier has a different SMS gateway address. 

This program is successfully runnning on a Pi3 with Raspian OS. 
