from src.db.connection import Connection
from src.db.db import Db


def test_criar_conexao():
    conn = Connection.create()
    assert conn is not None


def test_criar_db():
    conn = Connection.create()
    db_space = Db(conn)
    assert db_space is not None
