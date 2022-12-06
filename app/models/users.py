from app.core import db

def get_all():
    conn = db.dbconn()

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM app.users WHERE active = true ORDER BY name ASC')

    result = cursor.fetchall()

    conn.close()

    return result

def get(id):
    conn = db.dbconn()

    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM app.users where id = {}'.format(id))

    result = cursor.fetchone()

    conn.close()

    return result

def count():
    conn = db.dbconn()

    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM app.users WHERE active = true')

    result = cursor.fetchone()

    conn.close()

    return result