import os
import numpy as np
import datetime
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist

# ETAPA 1 pré processamento

# carregando a base de dados
# x_train(base de dados de treinamento) y_train(base de dados de teste)
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# print("base de dados", x_train)
#print("base de dados", x_train[0])
#ver classes
# print("base de dados", y_train)
#print("base de dados", y_train[0])

# ETAPA 2 normalizando as imagens
x_train = x_train / 255.0
x_test = x_test / 255.0
#print("base de dados", x_train[0])

# ETAPA 3 remodelando (reshaping) a base de dados (transformando em vetor)
# print("valor real", x_train.shape) #(60000, 28, 28)
# como a dimensão de cada imagem é 28x28, mudamos toda a base de dados para o formato (-1 (todos os elementos), altura * largura
x_train = x_train.reshape(-1, 28*28)
#print("valor alterado", x_train.shape) #(60000, 784)
# mudamos também a dimensão da base de teste
x_test = x_test.reshape(-1, 28*28)


# ETAPA 4 construindo a Rede Neural Artificial Densa
model = tf.keras.models.Sequential() #sequência de camadas
#print("ver tipo de classe", model)

# Adicionando uma camada densa de entrada (fully-connected)
model.add(tf.keras.layers.Dense(units=128, activation='relu', input_shape=(784, )))

# Adicionando a camada (Dropout) que prever o overffting
model.add(tf.keras.layers.Dropout(0.2)) #0.2 vamos zerar 20% dos neurônios dessa camada

# Adicionando a camada de saída (na bd temos 10 classes)
model.add(tf.keras.layers.Dense(units=10, activation="softmax"))



# ETAPA 5 Compilando o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])
#print(model.summary())

# ETAPA 6 Treninando o modelo
model.fit(x_train, y_train, epochs=5)

# ETAPA 7 Avaliação do modelo e previsão
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test accuracy: {}".format(test_accuracy))
print("Test loss ", test_loss)


