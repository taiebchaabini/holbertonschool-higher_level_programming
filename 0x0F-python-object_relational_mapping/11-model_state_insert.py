#!/usr/bin/python3
""" script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    new_element = 'Louisiana'
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name=new_element)
    session.add(new)
    query = session.query(State).filter_by(name=new_element).first()
    if (query is None):
        print("Not found")
        exit()
    print("{}".format(query.id))
    session.commit()
