import requests
import psycopg2

PGHOST = "ec2-54-172-126-94.compute-1.amazonaws.com"
PGDATABASE = "db2otnd9s7ld7n"
PGUSER = "fnjcktapkqvsyy"
PGPASSWORD = "ac177db6be80286cb03cf63c634cdd260d6d004db548936de9ca5b172488f5be"


class Article:
    def __init__(
        self,
        id: int,
        title: str,
        url: str,
        imageUrl: str,
        newsSite: str,
        summary: str,
        publishedAt: str,
        updatedAt: str,
        featured: bool,
        launches: list[str],
        events: list[str]
    ) -> None:
        self.id = id
        self.title = title
        self.url = url
        self.imageUrl = imageUrl
        self.newsSite = newsSite
        self.summary = summary
        self.publishedAt = publishedAt
        self.updatedAt = updatedAt
        self.featured = featured
        self.launches = launches
        self.events = events


print("Carga inicial dos dados no Banco de Dados")
base_url = "https://api.spaceflightnewsapi.net/v3"

r = requests.get(base_url + "/articles/count")
if r.status_code == 200:
    count = int(r.text)
    print(f"numero de artigos: {count}")

articles = []
r = requests.get(base_url + f"/articles?_limit={count}&_sort=id")
if r.status_code == 200:
    articles = [Article(**a) for a in r.json()]

m = 0
for a in articles:
    m = max(m, len(a.title))

print(m)

conn_string = "host=" + PGHOST + " port=" + "5432" + " dbname=" + PGDATABASE + " user=" + PGUSER + " password=" + PGPASSWORD

conn = psycopg2.connect(conn_string)
print("Connected!")

cursor = psycopg2.cursor()

sql = 
