from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\AvaJ84\\Downloads\\sqlite-3_10_1_win\\sqlite-3_10_1\\BCproject'
db = SQLAlchemy(app)


class FRequest(db.Model):
    __tablename__ = 'f_request'
##    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode, primary_key=True)
    description = db.Column('description', db.Unicode)
    client = db.Column('client', db.Unicode)
    priority = db.Column('priority', db.Integer)
    date = db.Column('date', db.Unicode)
    url = db.Column('url', db.Unicode)
    pArea = db.Column('pArea', db.Unicode)

    def __init__(self, title, description, client, priority, date, url, pArea):
##        self.id = id
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


@app.route('/')
def base_page():
    return render_template("basePage.html")


@app.route('/dblink2', methods=['GET', 'POST'])
def enter_data():
    new_request = FRequest(request.form['title'], request.form['description'],
                           request.form['client'], request.form['priority'], request.form['date'], request.form['url'], request.form['pArea'])
    db.session.add(new_request)
    db.session.commit()
    return " no problems"



@app.route('/dblink', methods=['GET', 'POST'])
def e_data():
    if request.method == 'POST':
        return request.form['title']
    else:
        return "no post"

if __name__ == '__main__':
    app.run()
