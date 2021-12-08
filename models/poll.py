from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import *
import hashlib
# player is an argument you can use with Game() >> Game(players=...)


class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Poll(Base):

    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    question_text = Column(String)

    # the input is stored in an instance variable (called an attribute)
    def __init__(self, answers, question_text):
        if len(answers) == 1:
            raise GameInitiationError("Games must include 2 or more players.")

        self.answers = answers
        self.question_text = question_text

    def answers(self):
        return self._answers

    def question_text(self):
        return self._question_text

