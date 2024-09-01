import pandas as pd
from tensorflow.keras.models import load_model
import functions as f
global model
import os
from CONSTANTES import CARPETA

#Importar los modelos
modelo_gender = load_model("data/modelos/clasificador_gender_2.h5")
modelo_etnia = load_model("data/modelos/clasificador_etnia.h5")

#Clasificar las imagenes
lista_imagenes = os.listdir(CARPETA)

diccionario = {"img_name": None, "gender": None, "etnia": None}

lista_gender = []
lista_etnia = []
imagenes = []

cont = 0

for img in lista_imagenes:
    imagenes.append(img)
    if f.predict_img(CARPETA + img, modelo_gender) == 0:
        lista_gender.append("H")
    else:
        lista_gender.append("M")

    if f.predict_img(CARPETA + img, modelo_etnia) == 0:
        lista_etnia.append("B")
    elif f.predict_img(CARPETA + img, modelo_etnia) == 1:
        lista_etnia.append("M")
    else:
        lista_etnia.append("N")
    cont += 1
    print(cont)
    #print(cont)

diccionario["img_name"] = imagenes
diccionario["gender"] = lista_gender
diccionario["etnia"] = lista_etnia

data_frame = pd.DataFrame(diccionario)
data_frame.to_csv("data/almacenamiento_general.csv", index=False)