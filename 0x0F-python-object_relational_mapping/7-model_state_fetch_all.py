#!/usr/bin/python3
"""Start link class to table in database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    connector = "mysql+mysqldb://{}:{}@localhost/{}".\
                format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(connector, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for row in states:
        print("{}: {}".format(row.id, row.name))
