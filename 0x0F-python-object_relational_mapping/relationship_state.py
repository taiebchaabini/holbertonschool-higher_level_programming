#!/usr/bin/python3
"""  python file that contains the class definition of a State and an instance
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, index=True, nullable=False,
            primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", order_by=City.id, back_populates="states")