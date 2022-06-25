import os
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator

image_folder = os.path.join('faces-recognition-dataset','faces95')
img_height, img_width = 250, 250 
num_classes = 2  

dataset = keras.preprocessing.image_dataset_from_directory(image_folder,seed=42,image_size=(img_height, img_width),label_mode='categorical',shuffle=True)

class_names = dataset.class_names
class_names

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(img_height, img_width, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    files = np.vstack([x])
    pred = face_classifier.predict(files, batch_size=32)
    print("Predicted: "+class_names[np.argmax(pred)])

from tensorflow import keras
face_classifier = keras.models.load_model("models/face_classifier_ResNet50.h5")
predict_image("faces-recognition-dataset/faces95/karyawan/max/max1.jpg")
def predict_image(image_path):
    img = image.load_img(image_path, target_size=(img_height, img_width, 3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    files = np.vstack([x])
    pred = face_classifier.predict(files, batch_size=32)
    print("Predicted: "+class_names[np.argmax(pred)])
    # hasil = class_names[np.argmax(pred)]
    # return hasil 


import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sideka',
                                         user='root',
                                         password='')
    value = (class_names(pred))
    query = "INSERT INTO history (data) VALUES (%s)"
    cursor = connection.cursor()
    cursor.execute(query,(value,))
    connection.commit()
    print("true")

except mysql.connector.Error as error:
    print("false".format(error))
    