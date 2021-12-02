from db.base import *
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import event
from models.poll import Poll

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    # level = Column(Integer, default=0)

    poll_id = Column(Integer, ForeignKey('polls.id'))
    poll = relationship(Poll, backref=backref('users', uselist=True, cascade='delete,all'))

    def __init__(self, first_name):
        self.first_name = first_name

    def full_name(self):
        return self.first_name

