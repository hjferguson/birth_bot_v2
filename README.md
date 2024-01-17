<h1>About</h1>

<h1>Set up</h1>

🟢[Download Python 3.10+](https://www.python.org/downloads/) and pip
(Keeping in mind your current version of python on your raspberry pi, if you are going to host there)

🟢Run the setup bash script from the terminal
    ./setup.sh

    You may not have permissions so run this and try again:
        chmod +x setup.sh

🟢After running the set up, add your credentials to .env and the people you want to message in birthdays.csv. For formatting, use a '+' followed by the country calling code, then the number. For the day and month entry, if single digit, just use the digit. Don't use '0'
    For example: 

    Correct:
    +11234567890,Harlan,3,30 ✅
    Bad Month:
    +11234567890,Harlan,03,30⛔
    Bad Day:
    +11234567890,Harlan,3,06 ⛔
    Bad Number:
    1234567890,Harlan,3,30   ⛔


🟢Run main.py when you are ready to start. I have it set up to run everyday at 9am using cron jobs on my Pi3. 

<h3>Important note for Pi deployment</h3>
Issues with SSL on Raspbian Python 3.9+
I ended up using python 3.7 and updating the requirements.txt to be compatible. 

