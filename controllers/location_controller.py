from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository

location_blueprint = Blueprint("locations", __name__)