import psycopg2


class Db:
    _db = None

    def __init__(self, conn):
        self._db = conn

    def checar_schema(self, schema: str):
        sql = f"""
        SELECT exists(
            SELECT
                nspname
            FROM
                pg_catalog.pg_namespace pn
            WHERE
                nspname='{schema}'
        ) AS schema_exists
        """
        cur = self._db.cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        cur.close()
        return rs[0]

    def criar_schema(self, schema: str):
        try:
            sql = f"CREATE SCHEMA {schema}"
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def checar_table(self, table: str, schema: str):
        sql = f"""SELECT exists(
                SELECT
                    tablename
                FROM
                    pg_catalog.pg_tables tb
                WHERE
                    tablename='{table}' and schemaname='{schema}'
        ) AS table_exists
        """
        cur = self._db.cursor()
        cur.execute(sql)
        rs = cur.fetchone()
        cur.close()
        return rs[0]

    def criar_table(self, table: str, schema: str, campos: str):
        try:
            sql = f"CREATE TABLE {schema}.{table}({campos})"
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def inserir_dados(self, table: str, schema: str, campos: str, dados: list):
        try:
            sql = f"INSERT INTO {schema}.{table} ({campos}) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self._db.cursor()
            for a in dados:
                cur.execute(sql, a.listar_dados())
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def recuperar_article(self, id: int, table: str, schema: str):
        rs = None
        try:
            sql = f"SELECT * FROM {schema}.{table} WHERE id={id}"
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchone()
        except:
            return None
        return rs

    def fechar(self):
        self._db.close()
