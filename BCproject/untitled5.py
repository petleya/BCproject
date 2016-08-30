from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_page

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)


@app.route('/')
def base_page():
    return render_template("basePage.html")


if __name__ == '__main__':
    app.run()
