import psycopg2, uuid
from datetime import datetime
from psycopg2.extras import DictCursor
conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='db')


def users_select_id_db(id):
    """ the function finds users id by telegram id from table transactions"""
    telegram_id = str(id)
    with conn:
        with conn.cursor(cursor_factory=DictCursor) as curs:
            curs.execute("SELECT u.id FROM USERS u WHERE u.telegram_id = %s", (telegram_id,))
            records = curs.fetchone()
            return records[0]

def users_select_db():
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

def transactions_select_db():
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

def users_insert_db():
    """this function inserts data about users  into table users"""
    with conn:
        with conn.cursor() as curs:
            curs.execute("INSERT INTO USERS (telegram_id, last_name, first_name, create_at) VALUES (111111111, 'Al', 'Ku', '2020-10-19')")
        conn.commit()

def users_delete_db():
    """ this functions deletes data from table users"""
    with conn:
        with conn.cursor() as curs:
            curs.execute("DELETE from USERS where telegram_id=111111111")
        conn.commit()

uuid1=uuid.uuid4()

def transactions_insert_db(created_by, result):
    """ this functions inserts data into table transactions"""
    with conn:
        with conn.cursor() as curs:
            curs.execute(" INSERT INTO TRANSACTIONS"
                         " (created_by, created_at, amount, for_what, creditor_id, debtor_id) "
                         "VALUES (%s, %s, %s, %s, %s, %s)", (created_by, datetime.now(), result[1], result[2], result[0], created_by))
        conn.commit()

