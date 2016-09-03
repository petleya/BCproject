from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import untitled5

untitled5.app.config['SQLALCHEMY_DATABASE_URI'] = "oniddb.cws.oregonstate.edu", "petleya-db", "h4QQvoY9jtkpIVYy", "petleya-db"
db = SQLAlchemy(untitled5.app)

class FRequest(db.Model):
    __tablename__ = 'f_requests'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode)
    description = db.Column('description', db.Unicode)
    client = db.Column('client', db.Unicode)
    priority = db.Column('priority', db.Integer)
    date = db.Column('date', db.Date)
    url = db.Column('url', db.Unicode)
    pArea = db.Column('pArea', db.Unicode)

    def __init__(self, id, title, description, client, priority, date, url, pArea):
        self.id = id
        self.title = title
        self.description = description
        self.client = client
        self.priority = priority
        self.date = date
        self.url = url
        self.pArea = pArea

    def __repr__(self):
        return '<FRequest %r>' % self.title

    db.create_all()