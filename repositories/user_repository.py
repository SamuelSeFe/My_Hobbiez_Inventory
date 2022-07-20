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

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        user = User(result['name'], result['current_energy'], result['time_available'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def update(user):
    sql = "UPDATE users SET (name, current_energy, time_available) = (%s, %s, %s) WHERE id = %s"
    values = [user.name, user.current_energy, user.time_available, user.id]
    run_sql(sql, values)

def completed_hobby(hobby, user_id):
    user = select(user_id)
    user_energy = user.current_energy - hobby.energy_expenditure
    user_time = user.time_available - hobby.duration
    user.current_energy = user_energy
    user.time_available = user_time
    update(user)
    