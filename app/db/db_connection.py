import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')

def select_db():
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM users')
            records = curs.fetchall()
            return records

def insert_db():
    with conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO USERS (telegram_id, last_name, first_name, create_at) VALUES (55555, 'Alex', 'Alexandr', '2020-09-10')")
        conn.commit()

def delete_db():
    with conn:
        with conn.cursor() as curs:
            curs.execute("DELETE from USERS where telegram_id=55555")
        conn.commit()



"""cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
records = cursor.fetchall()
cursor.close()
conn.close()

"""


"""
with closing(psycopg2.connect(...)) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM airport LIMIT 5')
        for row in cursor:
            print(row)

"""
