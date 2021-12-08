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

a = ""
while(a != "y" and a != "n"):
    a = input("Do you want to create a new poll? (response: y/n): ")

if a == "y":
    questionText = ""
    while(questionText == ""):
        questionText = str(input("What is your question? "))

    # Adds question mark to question if it is not there
    if questionText[-1] != '?':
        questionText += '?'

        print("Please make sure you have a question mark(?) at the end of your question next time.")
    else:
        pass
    isYesOrNo = ""
    while(isYesOrNo != "y" and isYesOrNo != "n"):
        isYesOrNo = input("Is this a Yes or No question? (responses: y/n) ")

    if isYesOrNo == "y":  # if it's yes or no, add those two answers to ses
        answer_list = [Answer(answer_text="Yes"),Answer(answer_text="No")]
        poll = Poll(answer_list)
        ses.add(poll)
        poll.question_text = str(questionText)
        ses.commit()

    elif isYesOrNo == "n":
        number_of_answers = None
        while(number_of_answers is None):
            try:
                number_of_answers = int(input("How many answers? "))
            except ValueError:
                print("Please enter an integer")

        answer_list = []

        for i in range(number_of_answers):
            answer_text = ""
            while(answer_text == ""):
                answer_text = input(f"Type your answer #{i+1} ")
            a = Answer(answer_text=answer_text)
            answer_list.append(a)

        print(f"adding {len(answer_list)} answers to a poll...")
        poll = Poll(answer_list)

        ses.add(poll)
        poll.question_text = str(questionText)
        ses.commit()
    else:
        print("Invalid response.")


if a == "n":
    print("Getting all the polls for you")
    #  query db for polls
    all_polls = ses.query(Poll).all()

    print("Here are the polls...")

    for poll in all_polls:
        print(f"-- [{poll.id}] {poll.question_text}")

    poll_id = None
    while(poll_id is None or poll_id > all_polls[-1].id or poll_id < all_polls[0].id):
        try:
            poll_id = int(input("Which poll (by id) do you want to view? "))
        except ValueError:
            print("Please enter an integer")

    poll = ses.query(Poll).get(poll_id)

    print(poll.question_text)
    print("Here are the answers: (select an id to answer!)")

    for answer in poll.answers:
        print(f"-- [{answer.id}] {answer.answer_text}")

    selection = None
    while(selection is None or selection > poll.answers[-1].id or selection < poll.answers[0].id):
        try:
            selection = int(input("What do you choose? "))
        except ValueError:
            print("Please enter an integer")



