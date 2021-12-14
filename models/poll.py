from sqlalchemy import Column, String, Integer
from db.base import *


class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Poll(Base):

    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    question_text = Column(String)

    # the input is stored in an instance variable (called an attribute)
    def __init__(self, answers):
        if len(answers) == 1:
            raise GameInitiationError("Polls must include 2 or more answers.")

        self.answers = answers

    def answers(self):
        return self._answers
