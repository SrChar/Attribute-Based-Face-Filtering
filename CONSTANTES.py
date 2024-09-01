import os

CARPETA = "data/imgs/"

DICCIONARIO_GENERO = {"Hombre": ["H"], "Mujer": ["M"], "Todos": ["H", "M"]}
DICCIONARIO_ETNIA = {"Blanco": ["B"], "Moreno": ["M"], "Negro": ["N"], "Todos": ["B", "M", "N"]}
DICCIONARIO_PELO = {"Corto": ["C"], "Medio": ["M"], "Largo": ["L"], "Todos": ["C", "M", "L"]}

OPCIONES_GENERO = ["Todos", "Hombre", "Mujer"]
OPCIONES_PELO = ["Todos", "Corto", "Medio", "Largo"]
OPCIONES_PIEL = ["Todos", "Negro", "Moreno", "Blanco"]

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

COMBOBOX_WIDTH = 80
COMBOBOX_HEIGHT = 25

IMG_WIDTH = 120
IMG_HEIGHT = 120

MARGEN_VERTICAL = 120
V_MARGEN = 50

N_IMGS = ( (SCREEN_WIDTH - COMBOBOX_WIDTH) / IMG_WIDTH) * ( (SCREEN_HEIGHT - MARGEN_VERTICAL) / IMG_HEIGHT )

directorio_raiz = (os.path.dirname(os.path.realpath("interfaz.py")))
directorio_raiz = directorio_raiz.replace("\\", "/")

if os.path.isdir(directorio_raiz + "/data/destino") is False:
    os.mkdir(directorio_raiz + "/data/destino")

CARPETA_DESTINO = directorio_raiz + "/data/destino"
LUGAR_ALMACENAMIENTO = "/data/almacenamiento.csv"
LISTA_IMGS = os.listdir(CARPETA_DESTINO)