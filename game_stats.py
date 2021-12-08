from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *

import numpy as np
import pandas as pd
from models.poll import Poll
from models.answer import Answer
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
#
# all_games = ses.query(Poll).all()
#
# print("Here are the polls...")
#
# for poll in all_games:
#     print(f"-- [{poll.id}] {poll.code}")
#
# game_id = int(input("Which game (by id) do you want to view? "))
#
#
#
# print(f"Cool. You have info on poll with code of {poll.code}")
# print("here are the players")
#
# for player in poll.players:
#     print(f"-- {player.first_name}")


def results(poll_id):
    poll = ses.query(Poll).get(poll_id)
    answers = poll.answers
    total_responses = len(answers)
    unique_values = set(answers)
    for i in unique_values:
        count = 0
        for k in range(len(answers)):
            if answers[k] == i:
                count += 1
        share = round((count/total_responses) * 100, 2)
        print(f'{i.answer_text}({share}%)')







