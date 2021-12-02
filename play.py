from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *

from models.poll import Poll
from models.player import User
import os
os.system("clear")

session = sessionmaker()

# setup db in folder 'db' and file name of farkle.sqlite
engine = create_engine(f"sqlite:///db/farkle.sqlite")
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

number_of_players = int(input("Do you want to create a new poll? "))
player_list = []

for i in range(number_of_players):
    name = input("What is the players name? ")
    u = User(first_name=name)
    player_list.append(u)

print(f"adding {len(player_list)} players to a game...")
game = Poll(players=player_list)

ses.add(game)
ses.commit()



print("Game On!")

game_active = True

while game_active:

    print(f"Player Up! {game.current_player().first_name}'s turn.")


    game_active = False