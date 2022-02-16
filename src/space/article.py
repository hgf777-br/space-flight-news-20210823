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
        launches: list[str],
        events: list[str]
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
