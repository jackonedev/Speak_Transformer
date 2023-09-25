from transformers import AutoTokenizer, AutoModelForSeq2SeqLM



## MODELOS: Ingles -> Español
model_en_es = "Helsinki-NLP/opus-mt-en-es"
tokenizer_en_es = AutoTokenizer.from_pretrained(model_en_es)
model_en_es = AutoModelForSeq2SeqLM.from_pretrained(model_en_es)

## MODELOS: Español -> Inglés
model_es_en = "Helsinki-NLP/opus-mt-es-en"
tokenizer_es_en = AutoTokenizer.from_pretrained(model_es_en)
model_es_en = AutoModelForSeq2SeqLM.from_pretrained(model_es_en)



def model_pipeline(language, text):
    if language == "es-en":
        tokenized_text = tokenizer_es_en(text, return_tensors="pt")
        translation = model_es_en.generate(**tokenized_text)
        translated = tokenizer_es_en.decode(translation[0], skip_special_tokens=True)

        
    if language == "en-es":
        tokenized_text = tokenizer_en_es(text, return_tensors="pt")
        translation = model_en_es.generate(**tokenized_text)
        translated = tokenizer_en_es.decode(translation[0], skip_special_tokens=True)
        translated = translated.replace("_", " ")

    return translated



if __name__ == "__main__":

    language = "es-en"
    print(f"Lenguaje seleccionado: {language}")

    text = input("Ingrese texto: ")

    translated = model_pipeline(language, text)
    print(translated)