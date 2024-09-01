"""
geregr
"""

import matplotlib.pyplot as plt
import numpy as np
import itertools
import pandas as pd
import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tkinter import *
from PIL import ImageTk, Image
from CONSTANTES import CARPETA, IMG_WIDTH, IMG_HEIGHT, SCREEN_WIDTH, N_IMGS, V_MARGEN, CARPETA_DESTINO, directorio_raiz, LUGAR_ALMACENAMIENTO, COMBOBOX_WIDTH
from tensorflow.keras.models import load_model
import shutil

def plotImages(images_arr):
    fig, axes = plt.subplots(1, 10, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    Esta funcion imprime y muestra el grafico de la confusion matrix
    La normalización puede ser aplicada pasándole 'normalize=True'
    :param cm:
    :param classes:
    :param normalize:
    :param title:
    :param cmap:
    :return:
    """

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

def predict_img(img_file, modelo):
    """
    Esta función se encarga de devolver el resultado de una predicción
    :param img_file:
    :param modelo:
    :return:
    """
    x = load_img(img_file, target_size=(96, 96))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arreglo = modelo.predict(x)
    resultado = arreglo[0]
    respuesta=np.argmax(resultado)
    return respuesta

def mostrar_imagenes(path, imagenes_mostradas, page):
    """
    Muestra las imágenes en pantalla según la pagina en la que se encuentre el usuario
    :param path:
    :param imagenes_mostradas:
    :param page:
    :return:
    """
    carpeta = path + "/"
    nombre_imagenes_mostradas = []
    for i in imagenes_mostradas:
        nombre_imagenes_mostradas.append(carpeta + i)
    margen_horizontal = 80
    img_mostrada = []
    lista_imgs_labels = []
    cont = 0
    fila = 0
    col = 0
    limite = int( (SCREEN_WIDTH - COMBOBOX_WIDTH) / IMG_WIDTH)
    limite2 = int((SCREEN_WIDTH - 80) / IMG_WIDTH)

    #print("page", page)
    minimo = int((N_IMGS * page) - N_IMGS)
    maximo = int(N_IMGS * page)
    if maximo >= len(nombre_imagenes_mostradas):
        maximo = len(nombre_imagenes_mostradas)

    for img in range(minimo, maximo):
        #print(img)
        i = Image.open(nombre_imagenes_mostradas[img]).resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        img_mostrada.append(ImageTk.PhotoImage(i))
        img_mostrada_label = Label(image=img_mostrada[cont])
        img_mostrada_label.image = img_mostrada[cont]
        img_mostrada_label.pack()
        img_mostrada_label.place(x=margen_horizontal + col * IMG_WIDTH, y=V_MARGEN + fila * IMG_HEIGHT)
        cont += 1
        col += 1
        if col == limite:
            fila += 1
            col = 0
        lista_imgs_labels.append(img_mostrada_label)
        #if fila >= (int(SCREEN_HEIGHT / IMG_HEIGHT)):
            #return lista_imgs_labels

    return lista_imgs_labels

def find_key(diccionario, key):
    """
    Devuelve la clave del diccionario que se le pase
    :param diccionario:
    :param key:
    :return:
    """
    return diccionario[key]

def predecir(carpeta_origen, barra_progreso=False, total_steps=1):
    """
    Se encarga de hacer las predicciones de las imágenes que se le pase
    Mueve las imágenes clasificadas a la carpeta de destino
    Añade los resultados al dataframe
    :param carpeta_origen:
    :param barra_progreso:
    :param total_steps:
    :return:
    """
    modelo_gender = load_model("data/modelos/clasificador_gender_2.h5")
    modelo_etnia = load_model("data/modelos/clasificador_etnia.h5")
    modelo_pelo = load_model("data/modelos/clasificador_pelo.h5")

    # Clasificar las imagenes
    lista_imagenes = os.listdir(carpeta_origen)
    diccionario = {"img_name": None, "gender": None, "etnia": None, "pelo": None}

    lista_gender = []
    lista_etnia = []
    lista_pelo = []
    imagenes = []


    cont = 0
    step = 0

    if barra_progreso != False:
        barra_progreso.place(x=590, y=100, width=200)

    for img in lista_imagenes:
        imagenes.append(img)
        if predict_img(carpeta_origen + "/" + img, modelo_gender) == 0:
            lista_gender.append("H")
        else:
            lista_gender.append("M")

        if predict_img(carpeta_origen + "/" + img, modelo_etnia) == 0:
            lista_etnia.append("B")
        elif predict_img(carpeta_origen + "/" + img, modelo_etnia) == 1:
            lista_etnia.append("M")
        else:
            lista_etnia.append("N")

        if predict_img(carpeta_origen + "/" + img, modelo_pelo) == 0:
            lista_pelo.append("C")
        elif predict_img(carpeta_origen + "/" + img, modelo_pelo) == 1:
            lista_pelo.append("M")
        else:
            lista_pelo.append("L")

        shutil.move(carpeta_origen + "/" + img, CARPETA_DESTINO + "/" + img)
        cont += 1
        #print(cont)

        if barra_progreso != False:
            barra_progreso.step(step)
            step += 18.1/total_steps
            #print(total_steps, 18.1/total_steps)
            barra_progreso.update()

        # print(cont)

    diccionario["img_name"] = imagenes
    diccionario["gender"] = lista_gender
    diccionario["etnia"] = lista_etnia
    diccionario["pelo"] = lista_pelo

    data_frame = pd.DataFrame(diccionario)
    #print("1", data_frame)
    if os.path.isfile(directorio_raiz + LUGAR_ALMACENAMIENTO) is False:
        data_frame.to_csv(directorio_raiz + LUGAR_ALMACENAMIENTO, index=False)
    else:
        data_frame_original = pd.read_csv(directorio_raiz + LUGAR_ALMACENAMIENTO)
        data_frame_original = data_frame_original.merge(data_frame, how="outer", on=["img_name", "gender", "etnia", "pelo"])
        data_frame_original.to_csv(directorio_raiz + LUGAR_ALMACENAMIENTO, index=False)

    n_men = len(list( data_frame[data_frame.gender.isin(["H"])]["img_name"] ))
    n_women = len(list( data_frame[data_frame.gender.isin(["M"])]["img_name"] ))

    n_black = len(list( data_frame[data_frame.etnia.isin(["N"])]["img_name"] ))
    n_brown = len(list( data_frame[data_frame.etnia.isin(["M"])]["img_name"] ))
    n_white = len(list( data_frame[data_frame.etnia.isin(["B"])]["img_name"] ))

    n_short = len(list( data_frame[data_frame.pelo.isin(["C"])]["img_name"] ))
    n_medium = len(list( data_frame[data_frame.pelo.isin(["M"])]["img_name"] ))
    n_large = len(list( data_frame[data_frame.pelo.isin(["L"])]["img_name"] ))

    return [n_men, n_women, n_black, n_brown, n_white, n_short, n_medium, n_large]