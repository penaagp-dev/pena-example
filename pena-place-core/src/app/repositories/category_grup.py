from src.app.repositories import __cursor__ as curr

def upsert(data):
    query = """
    INSERT INTO category_grup (nm_grup, is_no_use) VALUE(%s,%s) 
        ON DUPLICATE KEY UPDATE 
            nm_grup = VALUES(nm_grup),
            is_no_use=VALUES(is_no_use)
    """
    try:
        curr.execute(query, (data["grup_name"], data["is_no_use"]))
    except Exception as e:
        raise e
    else:
        curr
        return curr.lastrowid


def fetch_one(id):
    query = "SELECT * FROM category_grup WHERE id=%s and deleted_at is NULL"
    try:
        curr.execute(query, id)
    except Exception as e:
        raise e
    else:
        return curr.fetchone()


def fetch_all(limit, offset):
    query = "SELECT * FROM category_grup WHERE deleted_at is NULL LIMIT %s OFFSET %s"
    try:
        curr.execute(query, (limit, offset))
    except Exception as e:
        raise e
    else:
        return curr.fetchall()