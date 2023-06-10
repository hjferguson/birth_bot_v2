<h1>About</h1>

<h1>Set up</h1>

🟢[Download Python 3.10+](https://www.python.org/downloads/) and pip
(Keeping in mind your current version of python on your raspberry pi, if you are going to host there)

🟢Run the setup bash script from the terminal
    ./setup.sh

    You may not have permissions so run this and try again:
        chmod +x setup.sh

🟢After running the set up, add your credentials to .env and the people you want to message in birthdays.csv

🟢Run main.py when you are ready to start. I have it set up to run everyday at 12pm using cron jobs on my Pi3. 

