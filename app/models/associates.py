from app.core import db

def get_all():
    conn = db.dbconn()

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM app.associates WHERE active = true ORDER BY name ASC')

    result = cursor.fetchall()

    conn.close()

    return result

def get(cnpj):
    conn = db.dbconn()

    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM app.associates where cnpj = {}'.format(cnpj))

    result = cursor.fetchone()

    conn.close()

    return result

def count():
    conn = db.dbconn()

    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM app.associates WHERE active = true')

    result = cursor.fetchone()

    conn.close()

    return result