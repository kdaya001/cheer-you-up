import database

def get_all_cheer_ups():
    results = database.sql_select('select cheerups.cheerup, users.avatar_url, users.first_name, cheerups.rating FROM cheerups INNER JOIN users ON cheerups.user_id = users.id', ())
    return results

def insert_cheerup(cheerup, user_id):
    database.sql_write('INSERT INTO cheerups (user_id, cheerup, rating) VALUES (%s, %s, %s)', (user_id, cheerup, 0))

def get_user_cheerups(user_id):
    return database.sql_select('SELECT * FROM cheerups WHERE user_id = %s', [user_id])

def get_cheerup(id):
    return database.sql_select('SELECT * FROM cheerups WHERE id = %s', [id])

def remove_cheerup(id):
    return database.sql_write('DELETE FROM cheerups WHERE id = %s', [id])