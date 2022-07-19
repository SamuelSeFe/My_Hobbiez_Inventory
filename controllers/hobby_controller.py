from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.hobby import Hobby
import repositories.hobby_repository as hobby_repository
import repositories.location_repository as location_repository

hobby_blueprint = Blueprint("hobbies", __name__)

# INDEX
# GET '/hobbies'
@hobby_blueprint.route('/hobbies')
def hobbies():
    hobbies = hobby_repository.select_all()
    return render_template('hobbies/index.html', all_hobbies = hobbies)

# NEW
# GET '/hobby/new'
@hobby_blueprint.route('/hobby/new', methods=['GET'])
def new_hobby():
    locations = location_repository.select_all()
    return render_template('hobbies/new.html', all_locations = locations)

# CREATE
# POST '/hobbies'
@hobby_blueprint.route('/hobbies', methods=['POST'])
def create_hobby():
    name               = request.form['hobby_name']
    location_id        = request.form['location_id']
    duration           = request.form['hobby_duration']
    cost               = request.form['hobby_cost']
    energy_expenditure = request.form['hobby_energy_expenditure']
    completed          = request.form['hobby_completed']
    reminder           = request.form['hobby_reminder']
    location           = location_repository.select(location_id)
    hobby              = Hobby(name, location, duration, cost, energy_expenditure, reminder, completed)
    hobby_repository.save(hobby)
    return redirect('/hobbies')


# SHOW
# GET '/hobbies/<id>'
@hobby_blueprint.route('/hobbies/<id>', methods=['GET'])
def show_hobby(id):
    hobby = hobby_repository.select(id)
    return render_template('hobbies/show.html', hobby = hobby)

# EDIT
# GET '/hobbies/<id>/edit'
@hobby_blueprint.route('/hobbies/<id>/edit', methods=['GET'])
def edit_hobby(id):
    hobby = hobby_repository.select(id)
    location = location_repository.select_all()
    return render_template('hobbies/edit.html', hobby = hobby, all_locations = location)

# UPDATE
# PUT (POST) '/hobbies/<id>'
@hobby_blueprint.route('/hobbies/<id>', methods=['POST'])
def update_hobby(id):
    name               = request.form['hobby_name']
    location_id        = request.form['location_id']
    duration           = request.form['hobby_duration']
    cost               = request.form['hobby_cost']
    energy_expenditure = request.form['hobby_energy_expenditure']
    completed          = request.form['hobby_completed']
    reminder           = request.form['hobby_reminder']
    location           = location_repository.select(location_id)
    hobby              = Hobby(name, location, duration, cost, energy_expenditure, reminder, completed, id)
    hobby_repository.update(hobby)
    return redirect('/hobbies')

@hobby_blueprint.route('/hobbies/<id>/completed', methods=['POST'])
def completed_hobby(id):
    hobby_repository.hobby_completed(id)
    return redirect('/hobbies')


# DELETE
# DELTE (POST) '/hobbies/<id>
@hobby_blueprint.route('/hobbies/<id>/delete', methods=['POST'])
def delete_hobby(id):
    hobby_repository.delete(id)
    return redirect('/hobbies')