#!/usr/bin/python3
""" script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State, City
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).join(State.cities).\
        order_by(State.id, City.id).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}{}: {}".format("\t", city.id, city.name))
    session.close()
