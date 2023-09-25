from fastapi import FastAPI
from typing import Union
from enum import Enum
from model import model_pipeline

app = FastAPI()


class Language(str, Enum):
    es_en = "es-en"
    en_es = "en-es"


@app.get("/translate/{language}", status_code=200)
def translate(language: Language, text: Union[str, None] = None):

    if text is None:
        return {"error": "No text provided"}

    processed_text = model_pipeline(language, text)
    return {"translate": processed_text}



# Relevant refs:
# https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#create-an-enum-with-languages
