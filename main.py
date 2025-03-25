from typing import Union

from fastapi import FastAPI

from Program3 import add2 , muit2

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/add2/{arg}")
def add2_hander(arg:int):
    return {"arg": arg, "add2":add2(arg)}

@app.get("/muti2/{arg}")
def muti2_hander(arg:int):
    return {"arg": arg, "muti2":muit2(arg)}