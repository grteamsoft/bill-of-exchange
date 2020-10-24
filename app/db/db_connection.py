import psycopg2, uuid
from datetime import datetime
from psycopg2.extras import DictCursor
conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')


def transfer_select_db(id):
    """ the function finds users id by telegram id from table transactions"""
    telegram_id = str(id)
    with conn:
        with conn.cursor(cursor_factory=DictCursor) as curs:
            curs.execute("SELECT u.id FROM USERS u WHERE u.telegram_id = %s", (telegram_id,))
            records = curs.fetchone()
            return records[0]

def select_db():
    """ this functions outputs all data from table users"""
    with conn:
        with conn.cursor(cursor_factory=DictCursor) as curs:
            curs.execute('SELECT * FROM USERS')
            records = curs.fetchall()
            text = ''
            text1 = ''
            for record in records:
                for q in record:
                    text1 = text1 + str(q) + '  '
                text = text + '\n' + text1
                text1 = ''
            return text

def transaction_db():
    """ This functions outputs all data from table transactions"""
    with conn:
        with conn.cursor(cursor_factory=DictCursor) as curs:
            curs.execute('SELECT * FROM TRANSACTIONS')
            records = curs.fetchall()
            text = ''
            text1 = ''
            for record in records:
                for q in record:
                    text1 = text1 + str(q) + '  '
                text = text + '\n' + text1
                text1 = ''
            return text

def insert_db():
    """this function inserts data about users  into table users"""
    with conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO USERS (telegram_id, last_name, first_name, create_at) VALUES (111111111, 'Al', 'Ku', '2020-10-19')")
        conn.commit()

def delete_db():
    """ this functions deletes data from table users"""
    with conn:
        with conn.cursor() as curs:
            curs.execute("DELETE from USERS where telegram_id=55555")
        conn.commit()

uuid1=uuid.uuid4()

def insert_db_transactions(created_by, result):
    """ this functions inserts data into table transactions"""
    with conn:
        with conn.cursor() as curs:
            curs.execute(" INSERT INTO TRANSACTIONS"
                         " (created_by, created_at, amount, for_what, creditor_id, debtor_id) "
                         "VALUES (%s, %s, %s, %s, %s, %s)", (created_by, datetime.now(), result[1], result[2], result[0], created_by))
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
