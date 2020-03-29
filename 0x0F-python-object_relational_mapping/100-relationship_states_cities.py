#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa """
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, relationship
    from relationship_state import Base, State
    from relationship_city import City

    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
                 format(user, pwd, dbname)
    engine = create_engine(connection, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    """
    state_city_association = Table(                                                                      
            'state_city', Base.metadata,                                                
             Column('state_id', Integer, ForeignKey('states.id')),                       
             Column('city_id', Integer, ForeignKey('cities.id'))                         
    )                                                                           
    """
    new_state = State(name="California")
    new_city = City(name="San Fransico")
    new_state.cities = new_city
    session.add(new_state)
    session.add(new_city)
    session.commit()
