from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
from models import answer
import hashlib

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

print("#################################################")
print("############## Poll time! ######################")
print("#################################################")
print("\n\n")

a = input("Do you want to create a new poll? (response: y/n): ")
if a == "y":
    poll = Poll()
    ses.add(poll)
    questionText = input("What is your question? ")

    # Adds question mark to question if it is not there
    if questionText.split()[-1] != '?':
        questionText += '?'
        print("Please make sure you have a question mark(?) at the end of your question next time.")

    isYesOrNo = input("Is this a Yes or No question? (responses: y/n) ")

    if isYesOrNo == "y":  # if it's yes or no, add those two answers to ses
        answerText = "Yes"
        answer = Answer(answerText)
        ses.add(answer)

        answerText = "No"
        answer = Answer(answerText)
        ses.add(answer)
        print(answer)

        # ses.commit()

    elif isYesOrNo == "n":
        howManyAnswers = int(input("How many answers? "))

        for i in range(howManyAnswers):
            answerText = input("Type your answer: ")

            if answerText:
                answer = Answer(answerText=answerText)
                ses.add(answer)
            else:  # text is empty
                pass

if a == "n":
    print("Getting all the polls for you")
    #  query db for polls
    all_polls = ses.query(Poll).all()
    for poll in all_polls:
        print(f"-- [{poll.id}] {poll.questionText}")

    selection = int(input("Which poll (by id) do you want to view? "))

    answers = []

    query = ses.query(Answer).filter('poll_id' == selection)

    print(f"Cool. You have info on poll with code of {poll.id}")
    print("here are the questions")

    for answer in query:
        answers.append(answer)
        print(f"-- {answer.answerText}")

# poll = Poll()
#
# ses.add(poll)
# ses.commit()
