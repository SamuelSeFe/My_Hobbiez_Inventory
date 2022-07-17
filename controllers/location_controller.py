from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository

location_blueprint = Blueprint("locations", __name__)

# INDEX
# GET '/locations'

# NEW
# GET '/location/new'

# CREATE
# POST '/locations'

# SHOW
# GET '/locations/<id>'

# EDIT
# GET '/locations/<id>/edit'

# UPDATE
# PUT (POST) '/locations/<id>'

# DELETE
# DELTE (POST) '/locations/<id>