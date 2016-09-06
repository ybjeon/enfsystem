import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DB_NAME = '/grideye'

TABLE_DATA = 'table_data'
TABLE_UNIT = 'table_unit'

Base = declarative_base()

class Data(Base):
    __tablename__ = TABLE_DATA
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    datetime = Column(DateTime())
    value = Column(Float(10))


class Unit(Base):
    __tablename__ = TABLE_UNIT
    id = Column(Integer, primary_key=True)
    group = Column(String(10))
    latitude = Column(Float(10))
    longitude = Column(Float(10))

engine = create_engine('mysql://root:12345@localhost'+DB_NAME)

Base.metadata.create_all(engine)
