#!/usr/bin/python3
"""module"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
    
class State(Base):
    __tablename__ = "states"
    id = Column('id', Integer(), primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)

    def __init__(self, name):
        self.name = name

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
