import database

def insert_user(first_name, last_name, email, hashed_password, avatar):
    database.sql_write('INSERT INTO users (first_name, second_name, password, email, avatar_url, score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [first_name, last_name, hashed_password, email, avatar, 0])

def get_user_by_email(email):
    return database.sql_select('SELECT * FROM users WHERE email = %s', [email])

def get_user(user_id):
    return database.sql_select('SELECT * FROM users WHERE id = %s', [user_id])

def update_score(id):
    database.sql_write('UPDATE users SET score = score + 1 WHERE id = %s', [id])

def get_all_users():
    return database.sql_select('SELECT * FROM USERS ORDER BY score DESC', [])

def get_all_user_cheerups(id):
    return database.sql_select('SELECT users.id as userid, users.first_name, users.avatar_url, cheerups.id as cheerupsid, cheerups.rating, cheerups.cheerup, cheerups.weather from users LEFT JOIN cheerups on users.id = cheerups.id where users.id = %s ORDER BY rating DESC', [id])