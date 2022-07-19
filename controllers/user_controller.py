from unicodedata import name
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)

# INDEX
@user_blueprint.route('/users')
def user():
    user = user_repository.select(name)
    return render_template('user/index.html', user = user)
