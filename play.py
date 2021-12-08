from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *

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
print("############## Poll Time ######################")
print("#################################################")
print("\n\n")



a = input("Do you want to create a new poll? (response: y/n): ")
if a == "y":




    question_text = input("What is your question? ")

    # Adds question mark to question if it is not there
    if question_text.split()[-1] != '?':
        question_text += '?'
        print("Please make sure you have a question mark(?) at the end of your question next time.")

    isYesOrNo = input("Is this a Yes or No question? (responses: y/n) ")

    if isYesOrNo == "y":  # if it's yes or no, add those two answers to ses
        answer_list = [Answer(answer_text="Yes"),Answer(answer_text="No")]
        poll = Poll(answer_list, question_text)

        ses.add(poll)
        ses.commit()

    elif isYesOrNo == "n":

        number_of_answers = int(input("How many answers? "))
        answer_list = []

        for i in range(number_of_answers):
            answer_text = input("Type your answer ")
            a = Answer(answer_text=answer_text)
            answer_list.append(a)

        print(f"adding {len(answer_list)} players to a game...")
        poll = Poll(answer_list)

        ses.add(poll)
        ses.commit()



if a == "n":
    print("Getting all the polls for you")
    #  query db for polls
    all_polls = ses.query(Poll).all()
    for poll in all_polls:
        print(f"-- [{poll.id}] {poll.question_textext}")

    selection = int(input("Which poll (by id) do you want to view? "))

    answers = []

    query = ses.query(Answer).filter('poll_id' == selection)

    print(f"Cool. You have info on poll with code of {poll.id}")
    print("here are the questions")

    for answer in query:
        answers.append(answer)
        print(f"-- {answer.answerText}")




