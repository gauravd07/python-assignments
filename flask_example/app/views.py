from flask import render_template, request,flash, redirect, url_for
from app import app, db
from app.models import User


@app.route('/add' , methods=['POST', 'GET'])
def add():
    request_json_data = request.get_json()

    user_id = request_json_data.__getitem__('user_id')
    user_name = request_json_data.__getitem__('user_name')
    user = User(user_id,user_name)

    db.session.add(user)
    db.session.commit()

    flash("New entry was successfully posted")

    return "success"


@app.route('/')
def index():
    post = User.query.all()
    return post



