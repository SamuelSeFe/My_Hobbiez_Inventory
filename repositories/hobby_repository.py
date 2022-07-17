from db.run_sql import run_sql

from models.hobby import Hobby
from models.location import Location
import repositories.location_repository as location_repository

def save(hobby):
    sql = "INSERT INTO hobbies (name, location_id, duration, cost, energy_expenditure, reminder, completed) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [hobby.name, hobby.location.id, hobby.duration, hobby.cost, hobby.energy_expenditure, hobby.reminder, hobby.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    hobby.id = id
    return hobby

def select_all():
    hobbies = []

    sql = "SELECT * FROM hobbies"
    results = run_sql(sql)

    for row in results:
        location = location_repository.select(row['location_id'])
        hobby = Hobby(row['name'], location, row['duration'], row['cost'], row['energy_expenditure'], row['reminder'], row['completed'], row['id'])
        hobbies.append(hobby)
    return hobbies

def select(id):
    hobby = None
    sql = "SELECT * FROM hobbies WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
 
    if results:
        result = results[0]
        location = location_repository.select(result['location_id'])
        hobby = Hobby(result['name'], location, result['duration'], result['cost'], result['energy_expenditure'], result['reminder'], result['completed'], result['id'])
    return hobby

def delete_all():
    sql = "DELETE FROM hobbies"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM hobbies WHERE id = %s"
    values = [id]
    run_sql(sql, values)
