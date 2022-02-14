import psycopg2

PGHOST = "ec2-54-172-126-94.compute-1.amazonaws.com"
PGDATABASE = "db2otnd9s7ld7n"
PGUSER = "fnjcktapkqvsyy"
PGPASSWORD = "ac177db6be80286cb03cf63c634cdd260d6d004db548936de9ca5b172488f5be"

conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + \
    PGDATABASE + " user=" + PGUSER + " password=" + PGPASSWORD

conn = psycopg2.connect(conn_string)
print("Connected!")

cursor = conn.cursor()

sql = 'drop schema space'
cursor.execute(sql)
conn.commit()

