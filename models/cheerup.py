import database

def get_all_cheer_ups():
    results = database.sql_select('SELECT cheerups.cheerup, users.avatar_url, users.first_name, cheerups.rating, cheerups.id AS cheerupid, users.id AS userid, cheerups.voters, cheerups.weather FROM cheerups INNER JOIN users ON cheerups.user_id = users.id ORDER BY rating DESC', [])
    return results

def get_top_ten_cheer_ups():
    results = database.sql_select('SELECT cheerups.cheerup, users.avatar_url, users.first_name, cheerups.rating, cheerups.id as cheerupid, users.id as userid, cheerups.voters, cheerups.weather FROM cheerups INNER JOIN users ON cheerups.user_id = users.id ORDER BY rating DESC LIMIT 10', [])
    return results

def get_ten_most_recent_cheerups():
    results = database.sql_select('SELECT cheerups.cheerup, users.avatar_url, users.first_name, cheerups.rating, cheerups.id AS cheerupid, users.id AS userid, cheerups.voters, cheerups.weather FROM cheerups INNER JOIN users ON cheerups.user_id = users.id ORDER BY cheerups.timestamp DESC LIMIT 10', [])
    return results

def insert_cheerup(cheerup, user_id, weather):
    if weather == None:
        database.sql_write('INSERT INTO cheerups (user_id, cheerup, rating, voters) VALUES (%s, %s, %s, %s)', [user_id, cheerup, 0, []])
    else:
        database.sql_write('INSERT INTO cheerups (user_id, cheerup, rating, weather, voters) VALUES (%s, %s, %s, %s, %s)', [user_id, cheerup, 0, weather, []])

def get_user_cheerups(user_id):
    results = database.sql_select('SELECT cheerups.cheerup, users.avatar_url, users.first_name, cheerups.rating, cheerups.id AS cheerupid, users.id AS userid, cheerups.voters, cheerups.weather, users.score FROM cheerups INNER JOIN users ON cheerups.user_id = users.id WHERE users.id = %s ORDER BY rating DESC', [user_id])
    return results

def get_cheerup(id):
    return database.sql_select('SELECT * FROM cheerups WHERE id = %s', [id])

def delete_cheerup(id):
    database.sql_write('DELETE FROM cheerups WHERE id = %s', [id])

def upvote_cheerup(id):
    current_rating = database.sql_select('SELECT rating FROM cheerups WHERE id = %s', [id])
    new_rating = current_rating[0]['rating'] + 1
    database.sql_write('UPDATE cheerups SET rating = %s WHERE id = %s', [new_rating, id])

def update_voters(user_id, cheerup_id):
    database.sql_write('UPDATE cheerups SET voters = array_append(voters, %s) WHERE id = %s', [user_id, cheerup_id])