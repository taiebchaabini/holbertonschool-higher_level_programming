#!/usr/bin/python3
"""  python file that contains the class definition of a State and an instance
Base = declarative_base():"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sys import argv

user = argv[1]
pwd = argv[2]
dbname = argv[3]
Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    engine = create_engine("mysql+mysqldb://{}:{}@localhost\
            /{}".format(user, pwd, dbname))
    Base.metadata.create_all(engine)
