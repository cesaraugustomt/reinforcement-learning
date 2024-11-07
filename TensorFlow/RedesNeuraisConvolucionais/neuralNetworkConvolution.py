import os
import tensorflow as tf
import matplotlib.pyplot as plt
from sympy.physics.units.systems.si import units
from tensorflow.keras.datasets import cifar10
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics
from tensorflow.python.ops.gen_data_flow_ops import padding_fifo_queue_v2

# ETAPA 1 Pré-processamento
# configurando o nome das classes que serão previstas
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
# carregando a base de dados
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# ETAPA 2 normalização das imagens
x_train = x_train / 255.0
x_train.shape
x_test = x_test / 255.0
# mostrar imagem da classe
#plt.imshow(x_test[4])
#plt.show()

# ETAPA 3 Construindo a Rede Neural Convolucional
#definindo o modelo
model = tf.keras.models.Sequential()
# adicionando primeira camada de convolução / print o shape para saber o input_shape
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu", input_shape=[32, 32, 3]))
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu"))
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding='valid'))
# adicionando Flatten
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units=128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units=10, activation='softmax'))
print(model.summary())


# ETAPA 4 Compilando o modelo
# print(y_test[0]) # array([3]) sparse_categorical_crossentropy
# categorical_crossentropy -> # 0 0 0 1 0 0 0 0 0 0
model.compile(loss='sparse_categorical_crossentropy', optimizer="Adam", metrics=["sparse_categorical_accuracy"])

# ETAPA 5 Treinando o modelo
model.fit(x_train, y_train, epochs=15)

# ETAPA 6 Avaliando o modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test accuracy: {}".format(test_accuracy))
print("Test loss: {}" .format(test_loss))