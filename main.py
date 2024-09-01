from tkinter import *
from tkinter import ttk
import functions as f
import os

global lista_imgs_labels
import pandas as pd
from CONSTANTES import DICCIONARIO_ETNIA, DICCIONARIO_GENERO, DICCIONARIO_PELO, CARPETA, OPCIONES_GENERO, \
    OPCIONES_PIEL, OPCIONES_PELO, \
    COMBOBOX_HEIGHT, COMBOBOX_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, N_IMGS, CARPETA_DESTINO, LUGAR_ALMACENAMIENTO, \
    directorio_raiz, IMG_WIDTH, IMG_HEIGHT, V_MARGEN, MARGEN_VERTICAL
from tkinter import filedialog


# INTERFAZ
def seleccionador_genero_click(event):
    global lista_imgs_labels
    global page
    global lista_imgs
    global carpeta_origen

    for b in lista_imgs_labels:
        b.place_forget()

    page = 1

    data_frame_final = data_frame[data_frame.gender.isin(f.find_key(DICCIONARIO_GENERO, seleccionador_genero.get()))
                                  & data_frame.etnia.isin(f.find_key(DICCIONARIO_ETNIA, seleccionador_piel.get()))]

    lista_imgs = list(data_frame_final["img_name"])
    # print(data_frame)
    lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


def seleccionador_piel_click(event):
    global lista_imgs_labels
    global page
    global lista_imgs

    page = 1

    for b in lista_imgs_labels:
        b.place_forget()

    data_frame_final = data_frame[data_frame.gender.isin(f.find_key(DICCIONARIO_GENERO, seleccionador_genero.get()))
                                  & data_frame.etnia.isin(f.find_key(DICCIONARIO_ETNIA, seleccionador_piel.get()))]

    lista_imgs = list(data_frame_final["img_name"])
    # print(data_frame)
    lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


def seleccionador_pelo_click(event):
    global lista_imgs_labels
    global page
    global lista_imgs

    page = 1

    for b in lista_imgs_labels:
        b.place_forget()

    data_frame_final = data_frame[data_frame.gender.isin(f.find_key(DICCIONARIO_GENERO, seleccionador_genero.get()))
                                  & data_frame.etnia.isin(f.find_key(DICCIONARIO_ETNIA, seleccionador_piel.get()))
                                  & data_frame.pelo.isin(f.find_key(DICCIONARIO_PELO, seleccionador_pelo.get()))]

    lista_imgs = list(data_frame_final["img_name"])
    # print(data_frame)
    lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


# BUTTON FORWARD AND BACK#
def forward():
    global page
    global lista_imgs
    global lista_imgs_labels

    a = len(lista_imgs)
    if page <= int(a / N_IMGS):
        for b in lista_imgs_labels:
            b.place_forget()
        page += 1
        lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


def back():
    global page
    global lista_imgs
    global lista_imgs_labels

    if page > 1:
        for b in lista_imgs_labels:
            b.place_forget()

        page -= 1
        lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


def clasificar():
    ### BORRAR WIDGETS ###
    global lista_imgs_labels
    for b in lista_imgs_labels:
        b.place_forget()

    seleccionador_pelo.place_forget()
    seleccionador_genero.place_forget()
    seleccionador_piel.place_forget()
    button_back.place_forget()
    button_forward.place_forget()
    etiqueta_pelo.place_forget()
    etiqueta_genero.place_forget()
    etiqueta_piel.place_forget()

    button_carpeta_origen.place(x=0, y=300, width=80, height=40)
    button_ejecutar.place(x=0, y=400, width=80, height=40)


def abrir_carpeta_origen():
    global carpeta_origen
    carpeta_origen = filedialog.askdirectory(initialdir=directorio_raiz, title="Seleccione una carpeta")
    texto_carpeta_origen.config(text=carpeta_origen)
    texto_carpeta_origen.place(x=0, y=350)
    n_total_encontradas.configure(text="Se han encontrado " + str(len(os.listdir(carpeta_origen))) + " imágenes")


def ejecutar():
    global lista_imgs
    global data_frame
    try:
        resultados = f.predecir(carpeta_origen)
        lista_imgs = os.listdir(CARPETA_DESTINO)

        n_men.configure(text="Se han clasificado " + str(resultados[0]) + " hombres")
        n_women.configure(text="Se han clasificado " + str(resultados[1]) + " mujeres")
        n_black.configure(text="Se han clasificado " + str(resultados[2]) + " negros")
        n_brown.configure(text="Se han clasificado " + str(resultados[3]) + " morenos")
        n_white.configure(text="Se han clasificado " + str(resultados[4]) + " blancos")

        n_total_clasificadas.configure(
            text="Se han clasificado " + str(resultados[0] + resultados[1]) + " imágenes")
        n_total_encontradas.place(x=590, y=210)
        n_total_clasificadas.place(x=590, y=240)
        n_men.place(x=590, y=270)
        n_women.place(x=590, y=300)
        n_black.place(x=590, y=330)
        n_brown.place(x=590, y=360)
        n_white.place(x=590, y=390)
        n_short.place(x=590, y=420)
        n_medium.place(x=590, y=450)
        n_large.place(x=590, y=480)

        data_frame = pd.read_csv(directorio_raiz + LUGAR_ALMACENAMIENTO)
        # print(data_frame)

    except NameError:
        pass


def filtrar():
    global lista_imgs_labels
    global lista_imgs

    for b in lista_imgs_labels:
        b.place_forget()

    page = 1

    try:
        n_men.place_forget()
        n_women.place_forget()
        n_black.place_forget()
        n_brown.place_forget()
        n_white.place_forget()
        n_short.place_forget()
        n_medium.place_forget()
        n_large.place_forget()
        n_total_encontradas.place_forget()
        n_total_clasificadas.place_forget()
    except NameError:
        pass

    if "texto_carpeta_origen" in globals():
        texto_carpeta_origen.place_forget()

    try:
        button_ejecutar.place_forget()
        button_carpeta_origen.place_forget()
        barra_progreso.place_forget()
    except NameError:
        pass

    button_back.place(x=600, y=695)
    button_forward.place(x=680, y=695)

    seleccionador_pelo.place(x=0, y=293.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)
    seleccionador_genero.place(x=0, y=347.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)
    seleccionador_piel.place(x=0, y=401.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)

    etiqueta_pelo.place(x=0, y=274.5)
    etiqueta_genero.place(x=0, y=328.5)
    etiqueta_piel.place(x=0, y=382.5)

    lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)


def click_mouse(evento):
    global page
    x = root.winfo_pointerx() - root.winfo_rootx()
    y = root.winfo_pointery() - root.winfo_rooty()
    columna = int(((x + 40) / IMG_WIDTH))
    fila = int(((y + 70) / IMG_HEIGHT))
    if fila in range(1, int((SCREEN_HEIGHT - MARGEN_VERTICAL) / IMG_HEIGHT) + 1) and columna in range(1, int(
            (SCREEN_WIDTH - COMBOBOX_WIDTH) / IMG_WIDTH) + 1):
        lista_carpeta_destino = os.listdir(CARPETA_DESTINO)
        indice_img = int((columna + (fila * (SCREEN_WIDTH - COMBOBOX_WIDTH) / IMG_WIDTH) - 10) - 1)
        nombre_imagen.config(text=lista_carpeta_destino[indice_img + int((page - 1) * N_IMGS)])
        nombre_imagen.place(x=620, y=15)
    else:
        nombre_imagen.place_forget()
        # nombre_imagen.place_forget()
        # print(lista_carpeta_destino[indice_img + int((page - 1)* N_IMGS)])


def main():
    try:
        data_frame = pd.read_csv(directorio_raiz + LUGAR_ALMACENAMIENTO)
    except FileNotFoundError:
        diccionario = {"img_name": [None], "gender": [None], "etnia": [None], "pelo": [None]}
        data_frame = pd.DataFrame(diccionario)

    root = Tk()
    root.title("Image classificator")
    root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
    # root.resizable(False, False)

    page = 1
    lista_imgs = os.listdir(CARPETA_DESTINO)
    lista_imgs_labels = f.mostrar_imagenes(CARPETA_DESTINO, lista_imgs, page)

    # root.bind("<Motion>", mover_mouse)
    root.bind("<Button-1>", click_mouse)

    # NOMBRE IMAGEN
    nombre_imagen = Label(root, text="")
    texto_carpeta_origen = Label(root, text="")

    # NUMERO DE IMAGENES#
    n_total_clasificadas = Label(root, text="")
    n_total_encontradas = Label(root, text="")
    n_men = Label(root, text="")
    n_women = Label(root, text="")
    n_black = Label(root, text="")
    n_brown = Label(root, text="")
    n_white = Label(root, text="")
    n_short = Label(root, text="")
    n_medium = Label(root, text="")
    n_large = Label(root, text="")

    # BUTTON BACK AND FORWARD
    button_back = Button(root, text="<<", command=lambda: back())
    button_forward = Button(root, text=">>", command=lambda: forward())

    button_back.place(x=600, y=695)
    button_forward.place(x=680, y=695)
    ##############################################
    # BUTTON CLASIFICAR
    button_clasificar = Button(root, text="Clasificar", command=lambda: clasificar())
    button_clasificar.place(x=0, y=0, width=COMBOBOX_WIDTH, height=40)

    # BUTTON ORIGEN Y DESTINO
    button_carpeta_origen = Button(root, text="Origen", command=lambda: abrir_carpeta_origen())

    # BUTTON EJECUTAR
    button_ejecutar = Button(root, text="Ejecutar", command=lambda: ejecutar())

    # BUTTON FILTRAR
    button_filtrar = Button(root, text="Filtrar", command=lambda: filtrar())
    button_filtrar.place(x=0, y=50, width=COMBOBOX_WIDTH, height=40)

    # BARRA PROGRESO
    barra_progreso = ttk.Progressbar(root)

    # COMBOBOX DE PELO
    etiqueta_pelo = Label(root, text="Pelo")
    etiqueta_pelo.place(x=0, y=274.5)
    seleccionador_pelo = ttk.Combobox(root, value=OPCIONES_PELO)
    seleccionador_pelo.current(0)
    seleccionador_pelo.bind("<<ComboboxSelected>>", seleccionador_pelo_click)
    seleccionador_pelo.pack()
    seleccionador_pelo.place(x=0, y=293.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)

    # COMBOBOX DE GENERO
    etiqueta_genero = Label(root, text="Género")
    etiqueta_genero.place(x=0, y=328.5)
    seleccionador_genero = ttk.Combobox(root, value=OPCIONES_GENERO)
    seleccionador_genero.current(0)
    seleccionador_genero.bind("<<ComboboxSelected>>", seleccionador_genero_click)
    seleccionador_genero.pack()
    seleccionador_genero.place(x=0, y=347.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)

    # COMBOBOX DE PIEL
    etiqueta_piel = Label(root, text="Piel")
    etiqueta_piel.place(x=0, y=382.5)
    seleccionador_piel = ttk.Combobox(root, value=OPCIONES_PIEL)
    seleccionador_piel.current(0)
    seleccionador_piel.bind("<<ComboboxSelected>>", seleccionador_piel_click)
    seleccionador_piel.pack()
    seleccionador_piel.place(x=0, y=401.5, width=COMBOBOX_WIDTH, height=COMBOBOX_HEIGHT)

    # MOSTRAR IMAGENES#
    root.mainloop()
if __name__ == "__main__":
    main()