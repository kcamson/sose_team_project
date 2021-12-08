from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import *
import hashlib

class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Poll(Base):

    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    questionText = Column(String)

    def __init__(self, answers):
        self.answers = answers

    def answers(self):
        return self._answers



