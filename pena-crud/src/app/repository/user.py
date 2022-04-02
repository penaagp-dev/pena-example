from src.app.repository import __cursor__ as curr
from src.app.repository import __conn___ as conn

TABLE_USER = 'users'

def insert(data):
    try:
        q = "INSERT INTO "+TABLE_USER+" (name) VALUES (%s)"
        curr.execute(q, (data['name']))
    except Exception as e:
        raise e
    else:
        conn.commit()
        return curr.lastrowid

def find(limit=1, page=0):
    try:
        curr.execute("select * from "+TABLE_USER+" limit %s offset %s", (limit, page))
    except Exception as e:
        raise e
    else:
        return curr.fetchall()