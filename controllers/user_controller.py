from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)

# INDEX
@user_blueprint.route('/users')
def user():
    users = user_repository.select_all()
    return render_template('users/index.html', users = users)

# NEW
@user_blueprint.route('/user/new', methods=['GET'])
def new_user():
    return render_template('users/new.html')

# CREATE
@user_blueprint.route('/users', methods=['POST'])
def create_hobby():
    name               = request.form['user_name']
    current_energy     = request.form['user_current_energy']
    time_available     = request.form['user_time_available']
    user = User(name, current_energy, time_available)
    user_repository.save(user)
    return redirect('/users')

# SHOW
@user_blueprint.route('/users/<id>', methods=['GET'])
def show_user(id):
    user = user_repository.select(id)
    return render_template('users/show.html', user = user)

# UPDATE
@user_blueprint.route('/users/<id>', methods=['POST'])
def update_user(id):
    name                 = request.form['user_name']
    current_energy       = request.form['user_current_energy']
    time_available       = request.form['user_time_available']
    user = User(name, current_energy, time_available, id)
    user_repository.update(user)
    return redirect('/users')

