import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.optimizers import Adam
from preprocesador_imagenes import etnia_train_batches, etnia_valid_batches, etnia_test_batches
import functions
import os

height = 96
width = 96

modelo = Sequential([Conv2D(filters=32, kernel_size=(3,3), activation="relu", padding="same", input_shape=(height,width,3)),
                    MaxPool2D(pool_size=(2,2), strides=2),
                    Conv2D(filters=64, kernel_size=(3,3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2,2), strides=2),
                    Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2, 2), strides=2),
                    Conv2D(filters=256, kernel_size=(3, 3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2, 2), strides=2),
                    Flatten(),
                    Dense(units=128, activation="relu"),
                    #Dropout(0.2),
                    Dense(units=3, activation="softmax")])
                    #modelo.add(Dropout(0.1))
modelo.summary()
modelo.compile(optimizer=Adam(learning_rate=0.0005), loss="categorical_crossentropy", metrics=["accuracy"])
modelo.fit(x=etnia_train_batches, validation_data=etnia_valid_batches, batch_size=32, epochs=10, verbose=2)
if os.path.isfile("data/modelos/clasificador_etnia.h5") is False:
    modelo.save("data/modelos/clasificador_etnia.h5")