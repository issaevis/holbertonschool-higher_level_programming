#!/usr/bin/python3
"""model state class"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]
    st = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(u, p, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State.id).filter_by(name=sys.argv[4])
    if states.count() == 0:
        print('Not found')
    else:
        states = states.first()
        print("{}".format(states.id))
    session.close()