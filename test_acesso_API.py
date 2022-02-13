import requests

print("teste de acesso a API")
base_url = "https://api.spaceflightnewsapi.net/v3"

r = requests.get(base_url + "/articles/count")
if r.status_code == 200:
    count = r.text
    print(f"numero de artigos: {count}")

r = requests.get(base_url + "/articles?_limit=5&_sort=id")
if r.status_code == 200:
    articles = r.json()
    for a in articles:
        print(f"artigo id: {a['id']}")
        print(a['title'])
    print(articles[0])