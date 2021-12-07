from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
import os

from models.poll import Poll
from models.player import Answer
os.system('clear')

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/poll.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# you can use this variable to add and commit your changes
ses = session()

game = Poll(players=[player,player2])

print(game.id, game.code)