from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
import os

from models.poll import Poll
from models.player import User
os.system('clear')

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/farkle.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# you can use this variable to add and commit your changes
ses = session()

player = Player("Jack")
player2 = Player("Jill")

game = Game(players=[player,player2])

print(game.id, game.code)