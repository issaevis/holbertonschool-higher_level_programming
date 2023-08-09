#!/usr/bin/python3
"""module for state class"""
from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''state class'''
    __tablename__ = "states"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column('name', String(128), nullable=False)
