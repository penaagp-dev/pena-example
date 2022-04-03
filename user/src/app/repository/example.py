from src.app.repository import __cursor__ as curr
from src.app.repository import __conn___ as conn

def insert(data):
    try:
        curr.execute("INSERT INTO users (name) VALUES (%s)", (data['name']))
    except Exception as e:
        raise  e 
    else:
        conn.commit()
        return curr.lastrowid

def find(limit=1, page=0):
    try:
        curr.execute("select * from users limit %s offset %s", (limit, page))
    except Exception as e:
        raise e 
    else:
        return curr.fetchall()

def fetch(id):
    try:
        curr.execute("select * from users where id=%s", (id))
    except Exception as e:
        raise e
    else:
        return curr.fetchone()

def delete(id):
    try:
        curr.execute("DELETE FROM users WHERE id=%s", (id))
    except Exception as e:
        raise e
    else:
        conn.commit()
        return True

def update(id, data):
    try:
        curr.execute("UPDATE users SET name=%s WHERE id=%s", (id, data['name']))
    except Exception as e:
        raise e
    else:
        curr.execute("select * from users where id=%s", (id))
        return curr.fetchone()