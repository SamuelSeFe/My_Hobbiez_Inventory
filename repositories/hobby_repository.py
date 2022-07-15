from db.run_sql import run_sql

from models.hobby import Hobby
from models.location import Location
import repositories.location_repository as location_repositories

def save(hobby):
    sql = "INSERT INTO hobbies (name, description, duration, cost, energy_expenditure, reminder, competed) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [hobby.name, hobby.description, hobby.duration, hobby.cost, hobby.energy_expenditure, hobby.reminder, hobby.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    hobby.id = id
    return hobby

