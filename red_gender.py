from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from preprocesador_imagenes import gender_train_batches, gender_valid_batches
import os

modelo = Sequential([Conv2D(filters=16, kernel_size=(3,3), activation="relu", padding="same", input_shape=(96,96,3)),
                    MaxPool2D(pool_size=(2,2), strides=2),
                    Conv2D(filters=32, kernel_size=(3,3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2,2), strides=2),
                    Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2, 2), strides=2),
                    Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2, 2), strides=2),
                    Conv2D(filters=256, kernel_size=(3, 3), activation="relu", padding="same"),
                    MaxPool2D(pool_size=(2, 2), strides=2),
                    Flatten(),
                    Dense(units=128, activation="relu"),
                    Dense(units=2, activation="softmax")])
modelo.summary()
modelo.compile(optimizer=Adam(learning_rate=0.0005), loss="categorical_crossentropy", metrics=["accuracy"])
modelo.fit(x=gender_train_batches, validation_data=gender_valid_batches, batch_size=64, epochs=4, verbose=2)
if os.path.isfile("data/modelos/clasificador_gender.h5") is False:
    modelo.save("data/modelos/clasificador_gender.h5")