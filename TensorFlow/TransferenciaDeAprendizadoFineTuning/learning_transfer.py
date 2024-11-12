import os
import zipfile
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from param import output

from tensorflow.keras.preprocessing.image import ImageDataGenerator

#configurando caminho
dataset_path_new = "./cats_and_dogs_filtered"
train_dir = os.path.join(dataset_path_new, 'train')
validation_dir = os.path.join(dataset_path_new, 'validation')

# Construindo o modelo
# Carregamento do modelo pré-treinado
img_shape = (128, 128, 3) #valor pré configurado imagenet
base_model = tf.keras.applications.MobileNetV2(input_shape = img_shape,
                                               include_top = False,
                                               weights = 'imagenet')
#print(base_model.summary())

# Congelamento do modelo base
base_model.trainable = False

# Definição do cabeçalho personalizado da rede neural
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()(base_model.output) #calcula a média dos outputs para otimização
#https://arinjoyemail.medium.com/object-localization-using-global-average-pooling-layers-5e5fa0fda5f9#:~:text=The%20main%20idea%20is%20that,the%20image%2C%20localized%20in%20space.
#print(global_average_layer)
prediction_layer = tf.keras.layers.Dense(units = 1, activation = "sigmoid")(global_average_layer)

#Definindo o modelo
model = tf.keras.models.Model(inputs = base_model.input, outputs = prediction_layer)
#print(model.summary())

#Compilando o modelo
model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0001),
              loss="binary_crossentropy", metrics=["accuracy"])


#Criando geradores de dados (Data Generators)
#redimensionando as imagens
data_gen_train = ImageDataGenerator(rescale=1/255.)#transforma em float
data_gen_valid = ImageDataGenerator(rescale=1/255.)

train_generator = data_gen_train.flow_from_directory(train_dir, target_size=(128,128), batch_size=128, class_mode='binary')
valid_generator = data_gen_train.flow_from_directory(validation_dir, target_size=(128,128), batch_size=128, class_mode='binary')

# Treinando o modelo
model.fit(train_generator, epochs=2, validation_data=valid_generator)

# Avaliação do modelo de transferência de aprendizagem
valid_loss, valid_accuracy = model.evaluate(valid_generator)
print("accuracy:", valid_accuracy)
print("loss:", valid_loss)


