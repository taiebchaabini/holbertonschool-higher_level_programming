#!/usr/bin/python3
"""  python file that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """ this class represents the states table """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, index=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")
