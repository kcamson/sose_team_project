from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
import hashlib

from models.poll import Poll
from models.player import User
import os

os.system("clear")

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/poll.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# you can use this variable to add and commit your changes
ses = session()

print("#################################################")
print("############## Poll time! ######################")
print("#################################################")
print("\n\n")

initialQuestion = input("Do you want to create a new poll? (response: y/n): ")

while True:
    a = input("Do you want to create a new poll? (response: y/n): ")
    if a == "y":
        print("Taking you to the poll maker...")
        break
    if a == "n":
        print("Getting all the polls for you")
        break
    else:
        print("Try again")

userId = str(hashlib.md5())[-7:-1]
user = User('123')
poll = Poll(user)

ses.add(poll)
ses.commit()

