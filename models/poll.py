from sqlalchemy import Column, String, Integer, Array, PickleType, ForeignKey
from sqlalchemy.orm import relationship, backref
from db.base import *
import hashlib
# player is an argument you can use with Game() >> Game(players=...)


class GameInitiationError(Exception):
    def __init__(self, message):
        self.message = message


class Poll(Base):

    __tablename__ = 'polls'
    pollId = Column(Integer, primary_key=True)
    questionText = Column(String, default=1)
    answers = Column(Array)
    responders = Column(PickleType)

    # the input is stored in an instance variable (called an attribute)
    def __init__(self, user):
        if len(user) == 0:
            raise GameInitiationError("Poll must include a user.")

        self.user = user
        self.pollId = str(hashlib.md5())[-7:-1]

    def user(self):
        return self._user

