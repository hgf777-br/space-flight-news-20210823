import psycopg2

PGHOST = "ec2-34-206-148-196.compute-1.amazonaws.com"
PGDATABASE = "d6q0cel9pmg7c"
PGUSER = "rlwulmwptgnxah"
PGPASSWORD = "fad69ef6ffca471156c66f2d901fe9735d8bd66e790809a7f11e25d6b545c024"


class Connection:
    @staticmethod
    def create():
        conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + \
            PGDATABASE + " user=" + PGUSER + " password=" + PGPASSWORD
        return psycopg2.connect(conn_string)
