import psycopg2
from db.connection import Connection
from db.db import Db

conn = Connection.create()
db_space = Db(conn)

if not db_space.checar_schema("space"):
    if db_space.criar_schema("space"):
        print("esquema criado")
    else:
        print("esquema não foi criado")

if not db_space.checar_table("articles", "space"):
    campos = """
            id int primary key,
            featured boolean,
            title varchar(255),
            url varchar(255),
            imageUrl varchar(511),
            newsSite varchar(100),
            summary varchar,
            publishedAt varchar(255),
            launch_id varchar(255),
            launch_provider varchar(100),
            events_id varchar(255),
            events_provider varchar(100)
    """
    if db_space.criar_table("articles", "space", campos):
        print("tabela criada")
    else:
        print("tabela não foi criada")

