from typing import Union

from fastapi import FastAPI
from model import model_pipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/translate/{language}")
def read_item(language: str, text: Union[str, None] = None):

    processed_text = model_pipeline(language, text)
    

    return {"translate": processed_text}