from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db.base import *
import os
os.system("clear")

session = sessionmaker()

# setup db in folder 'db' and file name of poll.sqlite
engine = create_engine(f"sqlite:///db/poll.sqlite")
session.configure(bind=engine)

# create all the tables
# delete db file to regenerate
Base.metadata.create_all(engine)

# Create db session
ses = session()


# Function to display poll answers and their percentages
def results(poll):
    answers = poll.answers
    total_responses = 0

    for a in answers:
        total_responses += a.response_count

    print(f'Total Responses: {total_responses}')
    print("[Answer: Count, Percentage]")

    for a in answers:
        share = round((a.response_count/total_responses) * 100, 2)
        print(f'{a.answer_text}: {a.response_count}, {share}%')
