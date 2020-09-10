import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='postgres', host='db:5432')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
records = cursor.fetchall()
cursor.close()
conn.close()



"""
with closing(psycopg2.connect(...)) as conn:
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM airport LIMIT 5')
        for row in cursor:
            print(row)

"""