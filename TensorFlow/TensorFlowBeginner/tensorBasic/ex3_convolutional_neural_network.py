# Convolutional Neural Networks with Sequential and Functional API
import os

from tensorflow.python.keras.losses import SparseCategoricalCrossentropy

from ex2_neural_network import x_train, y_train, x_test, y_test, outputs

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Temos 50.000 imagens de treinamento + 10.000 imagens de teste, cada imagem tem
# 30 x 30 pixels + cores RGB
from tensorflow.keras.datasets import cifar10 #https://www.cs.toronto.edu/~kriz/cifar.html

# essas linhas ajudam a resolver problemas com gpu
#physical_devices = tf.config.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

# step 1 - carregar o conjunto de dados
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
# calcular em float62 é desnecessário aqui
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# step 2 - começando com um modelo sequêncial
model = keras.Sequential(
    [   # altura 32, largura 32 e 3 canais que são o RGB
        keras.Input(shape=(32, 32, 3)), #same: é para manter 32x32 valid: mudará dependedo do tamanho do kernel 30x30
        layers.Conv2D(32, (3, 3), padding='valid', activation='relu'),
        layers.MaxPool2D(pool_size=(2,2)),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(128, 3, activation='relu'),
        # saída
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        # 10 nós de saída
        layers.Dense(10),
    ]
)

#Functional API
def my_model():
    inputs = keras.Input(shape=(32, 32, 3))
    x =  layers.Conv2D(32, 3)(inputs)
    x = layers.BatchNormalization()(x)
    x = keras.activations.relu(x)
    x = layers.MaxPooling2D()(x)
    x = layers.Conv2D(64, 5, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = keras.activations.relu(x)
    x = layers.Conv2D(128, 3)(x)
    x = layers.BatchNormalization()(x)
    x = keras.activations.relu(x)
    x = layers.Flatten()(x)
    x = layers.Dense(64, activation='relu')(x)
    outputs = layers.Dense(10)(x)
    model = keras.Model(inputs=inputs, outputs=outputs)
    return model

model = my_model()

#print(model.summary())
# step 3 compilar
model.compile(
     #função de perda cruzada é diferente de uma softmax
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=3e-4),
    metrics=["accuracy"]
)

# step 4 treinar o modelo definitivamente
model.fit(x_train, y_train, batch_size=64, epochs=10, verbose=2)
# fazendo avaliação de pontos do modelo no conjunto
model.evaluate(x_test, y_test, batch_size=64, verbose=2)


# Suggestionss

# 1. What accuracy can you get on the test set by training longer, increasing
# the model size, changing kernel sizes, etc?

# 2. What can you get by using a conv net instead?







