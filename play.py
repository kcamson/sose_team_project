from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
from models import player
import hashlib

from models.poll import Poll
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

a = input("Do you want to create a new poll? (response: y/n): ")
if a == "y":
    pollId = str(hashlib.md5())[-7:-1]
    questionText = input("What is your question? ")

    # Adds question mark to question if it is not there
    if questionText.split()[-1] != '?':
        questionText += '?'
        print("Please make sure you have a question mark(?) at the end of your question next time.")

    print(questionText)

    isYesOrNo = input("Is this a Yes or No question? (responses: y/n) ")

    if isYesOrNo == "y":  # if it's yes or no, add those two answers to ses
        answerText = "Yes"
        answerId = str(hashlib.md5())[-7:-1]
        answer = player.Answer(answerText=answerText, answerId=answerId, pollId=pollId)
        ses.add(answer)

        answerText = "No"
        answerId = str(hashlib.md5())[-7:-1]
        answer = player.Answer(answerText=answerText, answerId=answerId, pollId=pollId)
        ses.add(answer)

    elif isYesOrNo == "n":
        howManyAnswers = int(input("How many answers? "))

        for i in range(howManyAnswers):
            answerText = input("Type your answer: ")

            if answerText:
                answerId = str(hashlib.md5())[-7:-1]
                answer = player.Answer(answerText=answerText, answerId=answerId, pollId=pollId)
                ses.add(answer)
            else:  # text is empty
                pass

if a == "n":
    print("Getting all the polls for you")

poll = Poll()

ses.add(poll)
ses.commit()
