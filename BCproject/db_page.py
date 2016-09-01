import untitled5
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
base = declarative_base()


class FRequest(base):
    __tablename__ = 'f_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(500))
    client = Column(String(50))
    priority = Column(Integer())
    date = Column(Date())
    url = Column(String(255))
    pArea = Column(String(50))

    base.metadata.create_all(untitled5.engine)