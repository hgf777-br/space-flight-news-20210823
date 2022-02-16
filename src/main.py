from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel
from src.db.connection import Connection
from src.db.db import Db

conn = Connection.create()
db_space = Db(conn)


class Launches(BaseModel):
    id: str
    provider: str


class Events(BaseModel):
    id: str
    provider: str


class Article(BaseModel):
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: list[Launches]
    events: list[Events]


class ArticleOut(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool
    launches: list[Launches]
    events: list[Events]


class Message(BaseModel):
    message: str


app = FastAPI()


@app.get("/", response_description="Home da nossa API")
async def root():
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


@app.get("/articles/", response_model=list[ArticleOut])
async def read_article_range(
    offset: int = Query(1,
                        title="offset",
                        description="id inicial para a lista de artigos.",
                        gt=0),
    limit: int = Query(10,
                       title="limite",
                       description="numero de artigos que serão retornados na lista.")
        ):
    return db_space.recuperar_article_range(offset, limit)


@app.get("/articles/{id}", response_model=ArticleOut, responses={404: {"model": Message}})
async def read_article(
    id: int = Path(...,
                   title="id do artigo",
                   description="id do artigo que deseja buscar")
        ):
    return db_space.recuperar_article(id)


@app.post("/articles/", response_model=ArticleOut)
async def create_article(article: Article):
    return db_space.inserir_article(article.dict())


@app.put("/articles/{id}", response_model=ArticleOut, responses={404: {"model": Message}})
async def change_article(
        id: int = Path(...,
                       title="id do artigo",
                       description="id do artigo que deseja alterar"),
        article: Article = Body(...)
        ):
    return db_space.editar_article(id, article.dict())


@app.delete("/articles/{id}", response_model=ArticleOut, responses={404: {"model": Message}})
async def delete_article(
    id: int = Path(...,
                   title="id do artigo",
                   description="id do artigo que deseja alterar"),
        ):
    return db_space.apagar_article(id)
