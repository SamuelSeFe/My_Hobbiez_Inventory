from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository
import repositories.hobby_repository as hobby_repository

location_blueprint = Blueprint("locations", __name__)

# INDEX
@location_blueprint.route('/locations')
def locations():
    locations = location_repository.select_all()
    return render_template('locations/index.html', all_locations = locations)

# NEW
@location_blueprint.route('/location/new', methods=['GET'])
def new_location():
    hobbies = hobby_repository.select_all()
    return render_template('locations/new.html', all_hobbies = hobbies)

# CREATE
@location_blueprint.route('/locations', methods=['POST'])
def create_location():
    name                 = request.form['location_name']
    description          = request.form['location_description']
    distance_to_location = request.form['location_distance_to_location']
    reminder             = request.form['location_reminder']
    location = Location(name, description, distance_to_location, reminder)
    location_repository.save(location)
    return redirect('/locations')

# SHOW
@location_blueprint.route('/locations/<id>', methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    return render_template('locations/show.html', location = location)

# EDIT
@location_blueprint.route('/locations/<id>/edit', methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    hobby = hobby_repository.select_all()
    return render_template('hobbies/edit.html', location = location, all_hobbies = hobby)

# UPDATE
@location_blueprint.route('/locations/<id>', methods=['POST'])
def update_location(id):
    name                 = request.form['location_name']
    description          = request.form['location_description']
    distance_to_location = request.form['location_distance_to_location']
    reminder             = request.form['location_reminder']
    location = Location(name, description, distance_to_location, reminder, id)
    location_repository.save(location)
    return redirect('/locations')

# DELETE
# DELTE (POST) '/hobbies/<id>
@location_blueprint.route('/locations/<id>/delete', methods=['POST'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/locations')