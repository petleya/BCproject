from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, Date
base = declarative_base()

class Request(base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(500))
    client = Column(String(50))
    priority = Column(Integer())
    date = Column(Date())
    url = Column(String(255))
    pArea = Column(String(50))