#!/usr/bin/python3
from model.user import User
from model import storage
import random
import string
from datetime import datetime, timedelta

# Function to generate a random string of fixed length
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate a random email
def random_email(length=20):
    domain = "@example.com"
    username = random_string(length - len(domain))
    return username + domain

# Function to generate a random date within the last 365 days
def random_date():
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    return start_date + (end_date - start_date) * random.random()

# Creating 20 more User instances
users = []
for _ in range(20):
    first_name = random_string(20)
    last_name = random_string(20)
    email = random_email()
    availableDate = random_date().date()
    occupation = "Employed"
    user = User(first_name=first_name, last_name=last_name, email=email, availableDate=availableDate, occupation=occupation )
    storage.new(user)
    storage.save()
