#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa """
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
