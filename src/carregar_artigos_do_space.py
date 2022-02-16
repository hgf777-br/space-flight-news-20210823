# Script para carregar os artigos do site https://spaceflightnewsapi.net/
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
print("Script para carregar os dados".center(40))
print("="*40 + "\n")

# Verificando quantos artigos o site Space possui
sp = Space()
count = sp.articles_count()
print(f"numero de artigos disponíveis: {count}\n")

# Carregando todos os arquivos do site Space
articles = sp.articles(count)

# Conexão com o Banco de Dados
conn = Connection.create()
db_space = Db(conn)

# Confere se o esquema já exite, e se não, cria o esquema
if not db_space.checar_schema(ESQUEMA):
    if db_space.criar_schema(ESQUEMA):
        print("esquema criado\n")
    else:
        print("esquema não foi criado\n")
else:
    print("esquema já existe\n")

# Confere se a tabela já exite, e se não, cria a tabela
if not db_space.checar_table(TABELA, ESQUEMA):
    if db_space.criar_table(TABELA, ESQUEMA, CAMPOS_CRIAR):
        print("tabela criada\n")
    else:
        print("tabela não foi criada\n")
else:
    print("tabela já existe\n")
    

# Carrega os artigos no Banco de Dados
print("Inserindo os dados, aguarde por favor (> 30 minutos)\n")
if db_space.inserir_dados(TABELA, ESQUEMA, CAMPOS, articles):
    print("Dados inseridos com sucesso")
else:
    print("Dados não inseridos")

# Fecha a conexão com o Banco de Dados
db_space.fechar()
