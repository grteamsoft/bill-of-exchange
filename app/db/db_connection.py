import psycopg2
conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='postgres', host='db:5432')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
records = cursor.fetchall()
cursor.close()
conn.close()
