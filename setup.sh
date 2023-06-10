#!/bin/bash

# Create and activate the virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Copy files
cp examp_birthdays.csv birthdays.csv 
cp example.env .env 

# Install packages from requirements.txt
pip install -r requirements.txt
