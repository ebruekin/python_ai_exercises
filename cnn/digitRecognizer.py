# -*- coding: utf-8 -*-
from sklearn.metrics import confusion_matrix
import itertools
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense ,Dropout,Flatten,Conv2D,MaxPool2D
from keras.optimizers import RMSprop,Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow import keras
from sklearn.model_selection import train_test_split
import tensorflow as tf

train = pd.read_csv("train.csv")
print(train.shape)
print(train.head())

print(" \n  ++++++++++++ yukarıdki train asagıdaki test++++++++++++++++ \n")

test = pd.read_csv("test.csv")
print(test.shape)
print(test.head())

Y_train = train["label"] # y rain dediğimiz şey bizim gercek, olması gereken train datamızdaki ilk column
X_train = train.drop(labels =["label"], axis = 1) # x train dediğimiz sey ise label dısındaki datamız


# dağılımı görmek için kücük analizler
plt.figure(figsize=(15,7))
sns.countplot(Y_train,palette= "icefire")
plt.title("digit class sayısı")
print(Y_train.value_counts())
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


img = X_train.iloc[3].as_matrix()
img =img.reshape((28,28))
plt.imshow(img,cmap="gray")
plt.title(train.iloc[3,0])
plt.axis("off")
plt.show()

#normalize
X_train = X_train/255.0
test = test/255.0
print("X_train :" , X_train.shape)
print("test :" , test.shape) 

X_train = X_train.values.reshape((-1,28,28,1))
test = test.values.reshape((-1,28,28,1))

print(X_train.shape)


Y_train =to_categorical(Y_train,num_classes=10) #label encoding


#test size yuzde 10 train size 100 de90 
#traain ile modelimi oluşturucam validation ile test edivem
X_train,X_val,Y_train,Y_val = train_test_split(X_train,Y_train,test_size=0.1,random_state=2)

print("x train shape :" ,X_train.shape)
print("x tes shape :" ,X_val.shape)
print("y train shape :" ,Y_train.shape)
print("y test shape :" ,Y_val.shape)


model = Sequential() #modelimizi tanımlamak için kullanılır

model.add(Conv2D(filters=8, kernel_size = (5,5),padding = 'Same',activation = 'relu',input_shape =(28,28,1)))
model.add(MaxPool2D(pool_size = (2,2)))
model.add(Dropout(0.25))

#

model.add(Conv2D(filters=16, kernel_size = (3,3),padding = 'Same',activation = 'relu'))
model.add(MaxPool2D(pool_size = (2,2),strides=(2,2)))
model.add(Dropout(0.25))

#♠ fully connected

model.add(Flatten())
model.add(Dense(256,activation = 'relu'))#input layer
model.add(Dropout(0.5))
model.add(Dense(10,activation = 'softmax'))# output layer, softmax sigmoidin gelişmişi diyebiliriz 

# adam optimizer = change the learning rate 

optimizer = Adam(lr=0.0001,beta_1=0.9,beta_2=0.999)

#compile the model

model.compile(optimizer=optimizer,loss="categorical_crossentropy",metrics=["accuracy"])

#epoch ve batchsize kavramı
epochs =10
batch_size =250

#augmented data
#data setimizde yeniden uretme yapıyoruz overfittingi onlemek için

datagen = ImageDataGenerator(
        featurewise_center = False,
        samplewise_center = False,
        featurewise_std_normalization=False,
        zca_whitening = False,
        rotation_range = 0.5, #randomly rotate images in the range 5 degrees
        zoom_range = 0.5 ,
        width_shift_range =0.5 ,
        height_shift_range =0.5 ,
        horizontal_flip= False,
        vertical_flip = False
    
        )      
datagen.fit(X_train)  
#fit the model


        
   

history = model.fit_generator(datagen.flow(X_train,Y_train,batch_size=batch_size),
                              epochs=epochs,validation_data=(X_val,Y_val),steps_per_epoch=X_train.shape[0]//batch_size)     






plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()




















