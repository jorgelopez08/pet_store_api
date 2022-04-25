"""Database models"""
from json.tool import main
from sqlalchemy import Column, Integer, String
from .database import Base

class Pet(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


