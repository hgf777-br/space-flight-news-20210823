import psycopg2

PGHOST = "ec2-54-172-126-94.compute-1.amazonaws.com"
PGDATABASE = "db2otnd9s7ld7n"
PGUSER = "fnjcktapkqvsyy"
PGPASSWORD = "ac177db6be80286cb03cf63c634cdd260d6d004db548936de9ca5b172488f5be"


class Connection:
    @staticmethod
    def create():
        conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + \
            PGDATABASE + " user=" + PGUSER + " password=" + PGPASSWORD
        return psycopg2.connect(conn_string)
