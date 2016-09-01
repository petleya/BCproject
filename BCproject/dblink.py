import untitled5
from flask import request
import db_page
from flask import Flask


@app.route('/dblink2', methods=['POST'])

def enter_data():
    new_request = db_page.FRequest(
        title=(request.args['title']),
        description=(request.args['description']),
        client=(request.args['client']),
        priority=(request.args['priority']),
        date=(request.args['date']),
        url=(request.args['url']),
        pArea=(request.args['area'])
    )
    untitled5.session.add(new_request)
    untitled5.session.commit()
