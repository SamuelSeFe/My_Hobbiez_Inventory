from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (name, current_energy, time_available) VALUES (%s, %s, %s) RETURNING *"
    values = [user.name, user.current_energy, user.time_available]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['current_energy'], row['time_available'], row['id'])
        users.append(user)
    return users

def select(name):
    user = None
    sql = "SELECT * FROM users WHERE name = %s"
    values = [name]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = User(result['name'], result['current_energy'], result['time_available'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)
