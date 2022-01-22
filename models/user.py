import database

def insert_user(first_name, last_name, email, hashed_password, avatar):
    database.sql_write('INSERT INTO users (first_name, second_name, password, email, avatar_url, score) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [first_name, last_name, hashed_password, email, avatar, 0])

def get_user_by_email(email):
    return database.sql_select('SELECT * FROM users WHERE email = %s', [email])

def get_user_by_id(id):
    return database.sql_select('SELECT * FROM users WHERE id = %s', [id])

def update_score(id):
    database.sql_write('UPDATE users SET score = score + 1 WHERE id = %s', [id])

def get_all_users():
    return database.sql_select('SELECT * FROM users ORDER BY score DESC', [])

def get_all_user_cheerups(id):
    return database.sql_select('SELECT users.id AS userid, users.score, users.first_name, users.avatar_url, cheerups.id AS cheerupid, cheerups.rating, cheerups.cheerup, cheerups.weather, cheerups.city, cheerups.public_visible, cheerups.voters FROM users LEFT JOIN cheerups ON users.id = cheerups.user_id WHERE users.id = %s ORDER BY rating DESC', [id])


def get_all_user_public_cheerups(id):
    return database.sql_select('SELECT users.id AS userid, users.score, users.first_name, users.avatar_url, cheerups.id AS cheerupid, cheerups.rating, cheerups.cheerup, cheerups.weather, cheerups.city, cheerups.public_visible, cheerups.voters FROM users LEFT JOIN cheerups ON users.id = cheerups.user_id WHERE users.id = %s AND cheerups.public_visible = True ORDER BY rating DESC', [id])

def get_password(id):
    return database.sql_select('SELECT id, password FROM users WHERE id = %s', [id])

def update_first_name(first_name, id):
    database.sql_write('UPDATE users SET first_name = %s WHERE id = %s', [first_name, id])

def update_last_name(last_name, id):
    database.sql_write('UPDATE users SET second_name = %s WHERE id = %s', [last_name, id])

def update_email(email, id):
    database.sql_write('UPDATE users SET email = %s WHERE id = %s', [email, id])

def update_password(hashed_password, id):
    database.sql_write('UPDATE users SET password = %s WHERE id = %s', [hashed_password, id])