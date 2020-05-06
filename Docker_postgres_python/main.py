# -*- coding: utf-8 -*-
from time import sleep

import psycopg2

if __name__ == '__main__':
    while True:
        try:
            conn = psycopg2.connect(dbname='postgres', user='docker', password='docker', host='my_postgres_sql')

            cursor = conn.cursor()
            cursor.execute('SELECT version()')
            print('Python says: %s' % cursor.fetchone()[0])

            cursor.close()
            conn.close()
        except Exception as e:
            print('ERROR: %s' % e)
        sleep(5)
