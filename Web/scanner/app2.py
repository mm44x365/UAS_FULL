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
def test_image_classifier_with_folder(model, path, y_true, img_height=250, img_width=250, class_names=['Penunggu','Karyawan']):
      
    num_classes = len(class_names)  
    total = 0  
    correct = 0 
    
    
    for filename in os.listdir(path):
        test_path = os.path.join(path, filename)
        test_image = image.load_img(
            test_path, target_size=(img_height, img_width, 3))
       
        
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        
       
        y_pred = class_names[np.array(result[0]).argmax(axis=0)]  
        iscorrect = 'correct' if y_pred == y_true else 'incorrect'
        print('{} - {}'.format(iscorrect, filename))
        for index in range(num_classes):
            print("\t{:6} with probabily of {:.2f}%".format(
                class_names[index], result[0][index] * 100))

        total += 1
        if y_pred == y_true:
            correct += 1

    print("\nTotal accuracy is {:.2f}% = {}/{} samples classified correctly".format(
        correct/total*100, correct, total))
    
    
from tensorflow import keras
face_classifier = keras.models.load_model("models/face_classifier_ResNet50.h5")
test_path = 'img/1.jpg'
test_image = image.load_img(test_path, target_size=(img_height, img_width, 3))
test_image

test_image = image.img_to_array(test_image) 
test_image = np.expand_dims(test_image, axis=0)
result = face_classifier.predict(test_image)

for index in range(num_classes):
    print("{:6} with probabily of {:.2f}%".format(
        class_names[index], result[0][index] * 100))
    
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='sideka',
                                         user='root',
                                         password='')
    value = (class_names[index])
    query = "INSERT INTO history (data) VALUES (%s)"
    cursor = connection.cursor()
    cursor.execute(query,(value,))
    connection.commit()
    print("true")

except mysql.connector.Error as error:
    print("false".format(error))
    
    
    