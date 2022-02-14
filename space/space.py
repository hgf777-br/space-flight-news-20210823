import requests
from space.article import Article

BASE_URL = "https://api.spaceflightnewsapi.net/v3"


class Space():

    def articles_count(self) -> int:
        r = requests.get(BASE_URL + "/articles/count")
        if r.status_code == 200:
            return int(r.text)
        else:
            return -1

    def articles(self, count: int) -> list:
        r = requests.get(BASE_URL + f"/articles?_limit={count}&_sort=id")
        if r.status_code == 200:
            return [Article(**a) for a in r.json()]
        else:
            return []
