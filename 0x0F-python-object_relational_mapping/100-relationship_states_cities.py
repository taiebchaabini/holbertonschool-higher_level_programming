#!/usr/bin/python3
""" script that creates the State “California” with the City “San Francisco”
from the database"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, relationship
    from relationship_state import Base, State, City
    from sqlalchemy import inspect

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    parent = State(name="California")
    parent.cities.append(City(name="San Francisco"))
    session.add(parent)
    session.commit()
