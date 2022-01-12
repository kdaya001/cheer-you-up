import database

def get_all_cheer_ups():
    results = database.sql_select('select cheerups.cheerup, avatar.url FROM cheerups INNER JOIN avatar ON cheerups.user_id = avatar.user_id', ())
    return results