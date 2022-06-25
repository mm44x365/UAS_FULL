import os
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

def get_classname(class_names, mask):
    assert len(class_names) == len(
        mask), "The arrays must be of the same length"

    return class_names[np.array(mask).argmax(axis=0)]

batch_size = 30
train_datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    brightness_range=(0.7, 1),
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=False,
    fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
    image_folder,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

n = 10

aug_image_folder = os.path.join('faces-recognition-dataset', 'faces_train_aug_images')
if not os.path.exists(aug_image_folder):
    os.makedirs(aug_image_folder) 
    
train_generator.save_to_dir = aug_image_folder
train_generator.save_format = 'jpg'

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping

from tensorflow.keras.preprocessing import image
train_image_folder = os.path.join('faces-recognition-dataset','face_dataset_train_images')
test_image_folder = os.path.join('faces-recognition-dataset','face_dataset_test_images')
img_height, img_width = 250, 250  
num_classes = 2  
validation_ratio = 0.15  
batch_size = 30

AUTOTUNE = tf.data.AUTOTUNE

train_ds = keras.preprocessing.image_dataset_from_directory(
    train_image_folder,
    validation_split=validation_ratio,
    subset="training",
    seed=42,
    image_size=(img_height, img_width),
    label_mode='categorical',
    batch_size=batch_size,
    shuffle=True)

val_ds = keras.preprocessing.image_dataset_from_directory(
    test_image_folder,
    validation_split=validation_ratio,
    subset="validation",
    seed=42,
    image_size=(img_height, img_width),
    batch_size=batch_size,
    label_mode='categorical',
    shuffle=True)

test_ds = keras.preprocessing.image_dataset_from_directory(
    test_image_folder,
    image_size=(img_height, img_width),
    label_mode='categorical',
    shuffle=False)

base_model = keras.applications.ResNet50(weights='imagenet',include_top=False,input_shape=(img_height, img_width, 3))
for layer in base_model.layers:layer.trainable = False

global_avg_pooling = keras.layers.GlobalAveragePooling2D()(base_model.output)
output = keras.layers.Dense(num_classes, activation='sigmoid')(global_avg_pooling)

face_classifier = keras.models.Model(inputs=base_model.input,outputs=output,name='ResNet50')
face_classifier.summary()

checkpoint = ModelCheckpoint("models/face_classifier_ResNet50.h5",monitor="val_loss",mode="min",save_best_only=True,verbose=1)
earlystop = EarlyStopping(monitor='val_loss',restore_best_weights=True, patience=3,verbose=1)
callbacks = [earlystop, checkpoint]

face_classifier.compile(loss='categorical_crossentropy',optimizer=keras.optimizers.Adam(learning_rate=0.01),metrics=['accuracy'])
epochs = 25
history = face_classifier.fit(
    train_ds,
    steps_per_epoch =6,
    epochs = 25,
    validation_data = val_ds,
    validation_steps = 1,
    verbose = 1,
    callbacks = [callbacks]
)
face_classifier.save("scanner/models/face_classifier_ResNet50.h5")
plt.figure(figsize=(16,12))
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.plot(history.history['val_accuracy'])
plt.plot(history.history['val_loss'])
plt.title('Model - Accuracy Vs Loss')
plt.xlabel('Epochs')
plt.legend(['Train Accuracy', 'Train Loss', 'Validation accuracy','Validation Loss'])
plt.show()