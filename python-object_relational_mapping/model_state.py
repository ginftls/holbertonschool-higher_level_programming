#!/usr/bin/python3
"""Defines the State class and links to the MySQL table 'states'."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    """Class definition for State."""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False,
                unique=True
                )
    name = Column(String(128), nullable=False)
