#!/usr/bin/python3
"""Script that prints all City objects from
    the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2],
                                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    result = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
