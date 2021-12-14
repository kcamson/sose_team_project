from db.base import *
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import event
from models.poll import Poll

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer_text = Column(String)
    response_count = Column(Integer, default=0)
    # level = Column(Integer, default=0)

    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship(Poll, backref=backref('answers', uselist=True, cascade='delete,all'))


    # __init__() gets executed when Player() is called
    # not necessary to include but very useful in most cases

    def __init__(self, answer_text):
        # self is a hook into the object created. It's how you add attributes
        self.answer_text = answer_text
        # the `_` signifies that the attribute should be treated as private


    def full_name(self):
        return self.answer_text

