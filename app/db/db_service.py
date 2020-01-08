import os
import psycopg2
from psycopg2.extras import DictCursor
from typing import Dict, List, Tuple


conn = psycopg2.connect(user="postgres", host="db")
cursor = conn.cursor()


def _init_db():
    with open(os.path.join("app", "db", "createdb.sql"), "r") as f:
        sql = f.read()
    cursor.execute(sql)
    conn.commit()


def check_db_exists():
    cursor.execute("""
SELECT COUNT(*)
FROM information_schema.tables 
WHERE 
    table_schema = 'public' AND 
    table_name = 'users'
""")
    table_exists = cursor.fetchone()[0]
    if table_exists:
        return
    _init_db()


check_db_exists()
