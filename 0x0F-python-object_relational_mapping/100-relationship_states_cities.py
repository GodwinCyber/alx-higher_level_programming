#!/usr/bin/python3
"""
    This script creates the State “California”
    with the City “San Francisco”
    from the database hbtn_0e_100_usa.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name="California")
    sf_city = City(name="San Francisco", state=cal_state)
    session.add(cal_state)
    session.add(sf_city)
    session.commit()
    session.close()
