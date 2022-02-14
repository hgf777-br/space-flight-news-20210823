# Script para carregar os artigos do site https://spaceflightnewsapi.net/
# para o nosso banco de dados Postgres no Heroku

import psycopg2
from space.space import Space
from db.connection import Connection
from db.db import Db

ESQUEMA = "space"
TABELA = "articles"
CAMPOS_CRIAR = """
    id_key serial primary key,
    id int,
    title varchar(255),
    url varchar(255),
    imageUrl varchar(511),
    newsSite varchar(100),
    summary varchar,
    publishedAt varchar(255),
    updateddAt varchar(255),
    featured boolean,
    launch_id varchar(255),
    launch_provider varchar(100),
    events_id varchar(255),
    events_provider varchar(100)
"""

CAMPOS = """
    id,
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

print("="*40)
print("Script para carregar os dados".center(40))
print("="*40 + "\n")

sp = Space()
count = sp.articles_count()
print(f"numero de artigos disponíveis: {count}\n")

articles = sp.articles(count)

conn = Connection.create()
db_space = Db(conn)

if not db_space.checar_schema(ESQUEMA):
    if db_space.criar_schema(ESQUEMA):
        print("esquema criado\n")
    else:
        print("esquema não foi criado\n")
else:
    print("esquema já existe\n")

if not db_space.checar_table(TABELA, ESQUEMA):
    if db_space.criar_table(TABELA, ESQUEMA, CAMPOS_CRIAR):
        print("tabela criada\n")
    else:
        print("tabela não foi criada\n")
else:
    print("tabela já existe\n")

print("Inserindo os dados, aguarde por favor (deve levar em torno de 30 minutos)\n")
if db_space.inserir_dados(TABELA, ESQUEMA, CAMPOS, articles):
    print("Dados inseridos com sucesso")
else:
    print("Dados não inseridos")
