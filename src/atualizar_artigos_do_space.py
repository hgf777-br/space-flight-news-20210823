# Script para carregar os artigos novos, diariamentedo, site https://spaceflightnewsapi.net/
# para o nosso banco de dados Postgres no Heroku

from space.space import Space
from db.connection import Connection
from db.db import Db

# Formato da Tabela no Banco de Dados
ESQUEMA = "space"
TABELA = "articles"
CAMPOS_CRIAR = """
    id serial primary key,
    id_space int,
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

print("="*40)
print("Script para carregar os novos artigos".center(40))
print("="*40 + "\n")

sp = Space()
conn = Connection.create()
db_space = Db(conn)

# descobrindo o id do ultimo artigo do site Space en nosso banco de dados
sql = f"SELECT id_space FROM {ESQUEMA}.{TABELA} ORDER BY id_space DESC LIMIT 1"
cur = conn.cursor()
cur.execute(sql)
id_ultimo = cur.fetchone()[0]
cur.close()
print(f"ultimo artigo importado em nosso Banco de Dados: {id_ultimo}\n")

# carregando do site Space os novos artigos  
articles = sp.new_articles(id_ultimo)
sz = len(articles)
if sz == 0:
    print("não foram encontrados novos artigos.\n")
elif sz == 1:
    print("foi encontrado 1 artigo novo\n")
else:
    print(f"foram encontrados {len(articles)} artigos novos\n")

# incluindo os novos artigos no nosso Banco de Dados
if sz > 0:
    print("Atualizando os dados, aguarde por favor\n")
    if db_space.inserir_dados(TABELA, ESQUEMA, CAMPOS, articles):
        print("Dados inseridos com sucesso")
    else:
        print("Dados não inseridos")

# fecha a conexão com o Banco de Dados
db_space.fechar()
