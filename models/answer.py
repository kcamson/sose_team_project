from db.base import *
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import event
from models.poll import Poll


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answerText = Column(String, primary_key=False)
    # level = Column(Integer, default=0)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship(Poll, backref=backref('answers', uselist=True, cascade='delete,all'))

    def __init__(self, answerText, pollId):
        self.answerText = answerText,
        self.poll_id = pollId
