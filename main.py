from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from db.connection import Connection
from db.db import Db

ESQUEMA = "space"
TABELA = "articles"

conn = Connection.create()
db_space = Db(conn)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Back-end Challenge 2021 🏅 - Space Flight News"}


@app.get("/articles/{id}")
async def read_item(id: int):
    return db_space.recuperar_article(id, TABELA, ESQUEMA)


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def change_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
