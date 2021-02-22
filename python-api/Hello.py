import psycopg2
import time

while True:
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='postgres' password='postgres'")
        print("Connected")
        break
    except Exception as e:
        print(e)
        time.sleep(3)


