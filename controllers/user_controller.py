from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)

# INDEX
@user_blueprint.route('/users')
def user():
    user = user_repository.select_all(name)
    return render_template('users/index.html', user = user)

# NEW
@user_blueprint.route('/user/new', methods=['GET'])
def new_user():
    return render_template('users/new.html')
