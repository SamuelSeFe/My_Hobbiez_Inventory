from db.run_sql import run_sql

from models.hobby import Hobby
from models.location import Location
import repositories.hobby_repository as hobby_repository

def save(location):
    sql = "INSERT INTO locations (name, description, distance_to_location, reminder) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [location.name, location.description, location.distance_to_location, location.reminder]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location

