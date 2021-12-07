from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *

from models.poll import Poll
from models.answer import User
from models.dice import StandardDie
from models.roll import Roll
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

all_games = ses.query(Poll).all()

print("Here are the polls...")

for poll in all_games:
    print(f"-- [{poll.id}] {poll.code}")

game_id = int(input("Which game (by id) do you want to view? "))

poll = ses.query(Poll).get(game_id)

print(f"Cool. You have info on poll with code of {poll.code}")
print("here are the players")

for player in poll.players:
    print(f"-- {player.first_name}")
