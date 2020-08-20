from sqlalchemy import Column, Integer, Float, String, Boolean, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Deaths(Base):
    __tablename__ == 'deaths'
    