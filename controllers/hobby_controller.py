from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.hobby import Hobby
import repositories.hobby_repository as hobby_repository

hobby_blueprint = Blueprint("hobbies", __name__)

# INDEX
# GET '/hobbies'

# NEW
# GET '/hobby/new'

# CREATE
# POST '/hobbies'

# SHOW
# GET '/hobbies/<id>'

# EDIT
# GET '/hobbies/<id>/edit'

# UPDATE
# PUT (POST) '/hobbies/<id>'

# DELETE
# DELTE (POST) '/hobbies/<id>