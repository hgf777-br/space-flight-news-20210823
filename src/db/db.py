from fastapi.responses import JSONResponse

ESQUEMA = "space"
TABELA = "articles"
CAMPOS = """
    id_space,
    title,
    url,
    imageUrl,
    newsSite,
    summary,
    publishedAt,
    updateddAt,
    featured,
    launch_id,
    launch_provider,
    events_id,
    events_provider
"""


class Db:
    def __init__(self, conn):
        self._db = conn

    # Rotinas para a inserção inicial dos dados

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

    # Rotinas para a API

    def _recuperar_ultimo_article(self):
        rs = None
        try:
            sql = f"SELECT * FROM {ESQUEMA}.{TABELA} ORDER BY id DESC LIMIT 1"
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchone()
            cur.close()
        except:
            return None
        ds = self._criar_dict(rs)
        return ds

    def recuperar_article(self, id: int):
        rs = None
        try:
            sql = f"SELECT * FROM {ESQUEMA}.{TABELA} WHERE id={id}"
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchone()
            cur.close()
        except:
            return None
        if rs is None:
            return JSONResponse(status_code=404, content={"message": "Não encontramos este ID na Base de Dados"})
        else:
            ds = self._criar_dict(rs)
            return ds

    def recuperar_article_range(self, offset: int, limit: int):
        rs = None
        try:
            sql = f"SELECT * FROM {ESQUEMA}.{TABELA} WHERE id>={offset} ORDER BY id LIMIT {limit}"
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
            cur.close()
        except:
            return None

        return [self._criar_dict(r) for r in rs]

    def apagar_article(self, id: int):
        ds = self.recuperar_article(id)
        try:
            sql = f"DELETE FROM {ESQUEMA}.{TABELA} WHERE id={id}"
            cur = self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return None
        return ds

    def inserir_article(self, article: dict):
        ds = list(article.values())
        ev = list(ds.pop()[0].values())
        la = list(ds.pop()[0].values())
        ds += (la + ev)
        try:
            sql = f"INSERT INTO {ESQUEMA}.{TABELA} ({CAMPOS}) VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self._db.cursor()
            cur.execute(sql, ds)
            cur.close()
            self._db.commit()
        except:
            return None
        return self._recuperar_ultimo_article()

    def editar_article(self, id: int, article: dict):
        ds = list(article.values())
        ev = list(ds.pop()[0].values())
        la = list(ds.pop()[0].values())
        ds += (la + ev)
        if isinstance(self.recuperar_article(id), dict):
            sql = f"""UPDATE {ESQUEMA}.{TABELA}
                    SET title = '{ds[0]}',
                        url = '{ds[1]}',
                        imageUrl = '{ds[2]}',
                        newsSite = '{ds[3]}',
                        summary = '{ds[4]}',
                        publishedAt = '{ds[5]}',
                        updateddAt = '{ds[6]}',
                        featured = '{ds[7]}',
                        launch_id = '{ds[8]}',
                        launch_provider = '{ds[9]}',
                        events_id = '{ds[10]}',
                        events_provider = '{ds[11]}'
                    WHERE id = {id}
                    """
            cur = self._db.cursor()
            cur.execute(sql, ds)
            cur.close()
            self._db.commit()
            return self.recuperar_article(id)
        return JSONResponse(status_code=404, content={"message": "Não encontramos este ID na Base de Dados"})

    def _criar_dict(self, rs):
        ds = {
            "id": rs[0],
            "title": rs[2],
            "url": rs[3],
            "imageUrl": rs[4],
            "newsSite": rs[5],
            "summary": rs[6],
            "publishedAt": rs[7],
            "updatedAt": rs[8],
            "featured": rs[9]
        }
        ds["launches"] = [{"id": rs[10], "provider": rs[11]}] if rs[10] != "" else []
        ds["events"] = [{"id": rs[12], "provider": rs[13]}] if rs[12] != "" else []

        return ds

    def fechar(self):
        self._db.close()
