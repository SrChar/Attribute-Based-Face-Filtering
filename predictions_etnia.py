from preprocesador_imagenes import etnia_test_batches
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix
import numpy as np
import functions as f
global model
import os

test_imgs, test_labels = next(etnia_test_batches)
model = load_model("data/modelos/clasificador_etnia.h5")
#print(type(test_imgs))
predicciones = model.predict(x=etnia_test_batches, verbose=0)
pred = np.round(predicciones)
#f.plotImages(test_imgs)
#print(test_labels)
#print(etnia_test_batches.classes)
#print(predicciones)
#print(np.round(predicciones))
#model.summary()
cm = confusion_matrix(y_true=etnia_test_batches.classes, y_pred=np.argmax(predicciones, axis=-1))
print(etnia_test_batches.class_indices)
cm_plot_labels = ["blancos", "morenos", "negros"]
f.plot_confusion_matrix(cm=cm, classes=etnia_test_batches.classes, title="Confusion Matrix")

imgs_blancos = os.listdir("data/etnia/test/blancos")
imgs_morenos = os.listdir("data/etnia/test/morenos")
imgs_negros = os.listdir("data/etnia/test/negros")

lista_etnias = imgs_blancos + imgs_morenos + imgs_negros
lista_blancos = []
lista_morenos = []
lista_negros = []
paths = ["data/etnia/test/blancos/",
         "data/etnia/test/morenos/",
         "data/etnia/test/negros/"]

for e in lista_etnias:
    print(e)
    respuesta = f.predict_etnia(e, model, paths)
    if respuesta == 0:
        lista_blancos.append(e)
    elif respuesta == 1:
        lista_morenos.append(e)
    else:
        lista_negros.append(e)

raw_data = [lista_blancos, lista_morenos, lista_negros]

f.export_dataframe(raw_data, ["blancos", "morenos", "negros"], "almacenamiento_etnias")