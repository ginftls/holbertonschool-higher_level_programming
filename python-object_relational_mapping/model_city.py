#!/usr/bin/python3
"""Model for the City class"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Class that defines the model of Cities table
    for the hbtn_0e_6_usa database"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
