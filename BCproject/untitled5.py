from flask import Flask, render_template, request
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


@app.route('/dblink2')
def enter_data():
    return "Hello, Ava!"
    new_request = db_page.FRequest(
        title='First Request',
        description='This is the request that is testing the database',
        client='Client A',
        priority=8,
        date='08/20/1984',
        url='http://yahoo.com',
        pArea='billing'
    )
    session.add(new_request)
    session.commit()


@app.route('/dblink', methods=['GET', 'POST'])
def e_data():
    if request.method == 'POST':
        return "yes post"
    else:
        return "no post"

if __name__ == '__main__':
    app.run()
