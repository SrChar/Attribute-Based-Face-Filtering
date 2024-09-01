from preprocesador_imagenes import gender_test_batches
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix
import numpy as np
import functions as f

test_imgs, test_labels = next(gender_test_batches)
model = load_model("data/modelos/clasificador_gender.h5")
predicciones = model.predict(x=gender_test_batches, verbose=0)
pred = np.round(predicciones)
cm = confusion_matrix(y_true=gender_test_batches.classes, y_pred=np.argmax(predicciones, axis=-1))
print(gender_test_batches.class_indices)
cm_plot_labels = ["men", "women"]
f.plot_confusion_matrix(cm=cm, classes=gender_test_batches.classes, title="Confusion Matrix")