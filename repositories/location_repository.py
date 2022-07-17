from db.run_sql import run_sql

from models.hobby import Hobby
from models.location import Location

def save(location):
    sql = "INSERT INTO locations (name, description, distance_to_location, reminder) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [location.name, location.description, location.distance_to_location, location.reminder]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location

def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['description'], row['distance_to_location'], row['reminder'], row['id'])
        locations.append(location)
    return locations

def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        location = Location(result['name'], result ['description'], result['distance_to_location'], result['reminder'], result['id'])
    return location

