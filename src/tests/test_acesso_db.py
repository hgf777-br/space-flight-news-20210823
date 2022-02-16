from src.db.connection import Connection
from src.db.db import Db


def criar_conexão():
    conn = Connection.create()
    assert conn is not None


def criar_Db():
    conn = Connection.create()
    db_space = Db(conn)
    assert db_space is not None
