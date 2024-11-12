import tensorflow as tf
import numpy as np

from tensorflow.keras.datasets import fashion_mnist

#print(tf.__version__)

#Etapa 1: Pré-processamento
#Carregando a base de dados FashionMNIST
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
#Normalização das imagens
X_train = X_train / 255.
X_test = X_test / 255.
#Mudando a dimensionalidade da base de dados
#print(X_train.shape) #(60000, 28, 28)
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)
#print(X_train.shape) #(60000, 784)

#Etapa 2: Construindo o modelo
#Definindo o modelo
model = tf.keras.models.Sequential()
#Construindo o modelo
model.add(tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784,)))
model.add(tf.keras.layers.Dropout(rate=0.2))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
#Compilando o modelo
#print(y_test) #array([9, 2, 1, ..., 8, 1, 5], dtype=uint8)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

#Etapa 3: Treinando o modelo
model.fit(X_train, y_train, epochs=2)

#Etapa 4: Avaliando o modelo
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test accuracy: {}".format(test_accuracy))

#Etapa 5: Convertendo o modelo para o TensorFlow Lite
#Salvando o modelo
model_name = "fashion_mobile_model.h5"
tf.keras.models.save_model(model, model_name)

#Criando o TFLite Converter
converter = tf.lite.TFLiteConverter.from_keras_model(model) #Alterado

#Convertendo o modelo
tflite_model = converter.convert()

#Salvando a versão TFLite
with open("tflite_model", "wb") as f:
  f.write(tflite_model)


# https://medium.com/@rdeep/tensorflow-lite-tutorial-easy-implementation-in-android-145443ec3775
# https://fritz.ai/neural-networks-on-mobile-devices-with-tensorflow-lite-a-tutorial/
# https://github.com/tensorflow/examples/tree/master/lite/examples
# https://www.tensorflow.org/lite/guide?hl=pt-br











