from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.hobby import Hobby
import repositories.hobby_repository as hobby_repository

hobby_blueprint = Blueprint("hobbies", __name__)