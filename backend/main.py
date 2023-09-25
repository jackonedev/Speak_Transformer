from fastapi import FastAPI
from typing import Union
from enum import Enum
from model import model_pipeline
from pydantic import BaseModel

app = FastAPI()

class Text(BaseModel):
    text: str


class Language(str, Enum):
    es_en = "es-en"
    en_es = "en-es"


@app.post("/translate/{language}", status_code=200)
def translate(language: Language, text: Text):

    processed_text = model_pipeline(language, text.text)
    return {"translate": processed_text}



# Relevant refs:
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#create-an-enum-with-languages
