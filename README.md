# Speak Transformers

Speak_Transformers es un proyecto de WEB API que implementa modelos de transformers para realizar traducciones de inglés a español y viceversa. El objetivo es ofrecer una solución de traducción rápida, precisa y de alta calidad para usuarios que necesiten comunicarse en diferentes idiomas. El proyecto utiliza la librería HuggingFace Transformers para implementar los modelos pre-entrenados de traducción, así como FastAPI para crear la interfaz web. El objetivo principal del proyecto consiste:

- Traducción bidireccional entre inglés y español
- (Próximamente) Carga de documentos .txt para traducir
- (Próximamente) Descarga de las traducciones en documentos .txt al disco local
- (Próximamente) Interfaz de usuario hecha en React.JS


## Documentación

La documentación detallada de la API se realiza automáticamente por medio de Swagger y también por medio de Redocly gracias a FastAPI.


## Ejemplo de uso


<img src="https://github.com/jackonedev/Speak_Trasnformer/blob/main/resources/example.gif?raw=true" heigth="750"/>


### Caso Español-Inglés:

**Texto:** Durante siglos, incluso milenios, los seres humanos han creído que en la mente humana existe un conflicto entre el bien y el mal. Pero eso no es verdad. El bien y el mal son sólo el resultado del conflicto, porque el conflicto real está entre la verdad y las mentiras.

**Traducción:** For centuries, even millennia, human beings have believed that in the human mind there is a conflict between good and evil. But that is not true. Good and evil are only the result of conflict, because the real conflict is between truth and lies.

### Caso Inglés-Español:

**Texto:** Genuine pride is the feeling obtained from the attainment of values established in the process of self-actualization. Neurotic pride is the feeling attained by the apparent attainment of one or more of the \"inner dictates\".

**Traducción:** El orgullo genuino es el sentimiento obtenido del logro de valores establecidos en el proceso de auto-actualización. El orgullo neurótico es el sentimiento alcanzado por el logro aparente de uno o más de los "dictantes internos".