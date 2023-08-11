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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(u, p, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    f_state = session.query(State).order_by(State.id)

    if state.count() == 0:
        print("Nothing")

    else:
        state = f_state.first()
        print("{}: {}".format(state.id, state.name))

    session.close()
