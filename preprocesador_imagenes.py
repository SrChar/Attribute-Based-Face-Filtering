import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


#PREPROCESSING ETNIA
etnia_train_path = "data/etnia/train"
etnia_valid_path = "data/etnia/valid"
etnia_test_path = "data/etnia/test"

etnia_train = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=30,
    shear_range=0.2,
    zoom_range=0.2,
)
etnia_valid = ImageDataGenerator(
    rescale=1./255
)
etnia_test = ImageDataGenerator(
    rescale=1./255
)

etnia_train_batches = etnia_train.flow_from_directory(directory=etnia_train_path,
target_size = (96,96), classes=["blancos", "morenos", "negros"], batch_size=32)
etnia_valid_batches = etnia_valid.flow_from_directory(directory=etnia_valid_path,
target_size = (96,96), classes=["blancos", "morenos", "negros"], batch_size=32)
etnia_test_batches = etnia_test.flow_from_directory(directory=etnia_test_path,
target_size = (96,96), classes=["blancos", "morenos", "negros"], batch_size=32, shuffle=False)


#PREPROCESSING
gender_train_path = "data/gender/train"
gender_valid_path = "data/gender/valid"
gender_test_path = "data/gender/test"

#PREPROCESSING GENDER
gender_train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    shear_range=0.2,
    zoom_range=0.2,
)
gender_valid_datagen = ImageDataGenerator(
    rescale=1./255,
)
gender_test_datagen = ImageDataGenerator(
    rescale=1./255
)

gender_train_batches = gender_train_datagen.flow_from_directory(directory=gender_train_path,
target_size=(96,96), classes=["men", "women"], batch_size=32)
gender_valid_batches = gender_valid_datagen.flow_from_directory(directory=gender_valid_path,
target_size=(96,96), classes=["men", "women"], batch_size=32)
gender_test_batches = gender_test_datagen.flow_from_directory(directory=gender_test_path,
target_size=(96,96), classes=["men", "women"], batch_size=32, shuffle=False)


#PREPARARTION HAIR
hair_train_path = "data/hair/train"
hair_valid_path = "data/hair/valid"
#hair_test_path = "data/hair/test"

#PREPROCESSING HAIR
hair_train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    shear_range=0.2,
    zoom_range=0.2,
    #height_shift_range=0.1,
    #horizontal_flip=True
)
hair_valid_datagen = ImageDataGenerator(
    rescale=1./255,
    #rotation_range = 30,
    #shear_range = 0.3,
    #zoom_range = 0.3,
)
hair_test_datagen = ImageDataGenerator(
    rescale=1./255
)

hair_train_batches = hair_train_datagen.flow_from_directory(directory=hair_train_path,
target_size=(96,96), classes=["corto", "medio", "largo"], batch_size=32)
hair_valid_batches = hair_valid_datagen.flow_from_directory(directory=hair_valid_path,
target_size=(96,96), classes=["corto", "medio", "largo"], batch_size=32)
