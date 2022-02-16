import requests

BASE_URL = "https://api.spaceflightnewsapi.net/v3"


class Article:
    def __init__(
        self,
        id: int,
        featured: bool,
        title: str,
        url: str,
        imageUrl: str,
        newsSite: str,
        summary: str,
        publishedAt: str,
        updatedAt: str,
        launches: list[dict],
        events: list[dict]
    ) -> None:
        self.id = id
        self.featured = featured
        self.title = title
        self.url = url
        self.imageUrl = imageUrl
        self.newsSite = newsSite
        self.summary = summary
        self.publishedAt = publishedAt
        self.updatedAt = updatedAt
        self.launches = launches
        self.events = events

    def listar_dados(self):
        res = [
            self.id,
            self.title,
            self.url,
            self.imageUrl,
            self.newsSite,
            self.summary,
            self.publishedAt,
            self.updatedAt,
            self.featured
        ]
        if len(self.launches) == 0:
            res.extend(["", ""])
        else:
            res.extend(self.launches[0].values())
        if len(self.events) == 0:
            res.extend(["", ""])
        else:
            res.extend(self.events[0].values())

        return res


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

    def new_articles(self, id: int) -> list:
        r = requests.get(BASE_URL + f"/articles?_sort=id&id_gt={id}")
        if r.status_code == 200:
            return [Article(**a) for a in r.json()]
        else:
            return []
