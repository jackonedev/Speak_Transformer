from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/translate/{language}")
def read_item(language: str, text: Union[str, None] = None):

    if language == "en-es":
        processed_text = text.upper()
        
        pass
    
    elif language == "es-en":
        processed_text = text.upper()
        pass

    else:
        return {"error": "language not supported"}
    
    
    return {"translate": processed_text}