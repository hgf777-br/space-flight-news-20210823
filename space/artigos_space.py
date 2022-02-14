import requests

BASE_URL = "https://api.spaceflightnewsapi.net/v3"


class Space():

    def articles_count(self):
        r = requests.get(BASE_URL + "/articles/count")
        if r.status_code == 200:
            return int(r.text)
        else:
            return -1


