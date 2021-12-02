from sqlalchemy import Column, String, Integer, ARRAY, PickleType, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import *
import hashlib


class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Poll(Base):

    __tablename__ = 'polls'
    id = Column(Integer, primary_key=True)
    questionText = Column(String, default=1)
    answers = Column(PickleType)
    responders = Column(PickleType)

    # the input is stored in an instance variable (called an attribute)
    def __init__(self, user):

        self.user = user
        self.pollId = str(hashlib.md5())[-7:-1]

    def user(self):
        return self._user

