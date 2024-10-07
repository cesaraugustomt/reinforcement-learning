# Neural Network
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #ignore mensagens do tensorflow

import tensorflow as tf
from tensorflow import keras, optimizers, metrics
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist #dataset de imagem de números de 1 a 9

#physical_devices = tf.config.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Carregar dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train.shape) # (60000, 28, 28)
# print(y_train.shape) # (60000,)

# precisamos achata-lo para enviar para uma rede neural
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0 #784 é o mesmo que 28*28
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0

x_train = tf.convert_to_tensor(x_train)

# passo 1 - criar um modelo
# Keras Sequential API (Very convenient, not very flexible)
model = keras.Sequential(
    [
        keras.Input(shape=(28*28)),
        layers.Dense(512, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(10)
    ]
)

#print(model.summary())

#_________________________________________________________________
#Layer (type)                 Output Shape              Param #
#=================================================================
#dense (Dense)                (None, 512)               401920
#_________________________________________________________________
#dense_1 (Dense)              (None, 256)               131328
#_________________________________________________________________
#dense_2 (Dense)              (None, 10)                2570
#=================================================================
#Total params: 535,818
#Trainable params: 535,818
#Non-trainable params: 0
#_________________________________________________________________

#import sys
#sys.exit()

# Depuração sequencial de camadas
model = keras.Sequential()
model.add(keras.Input(shape=(784)))
model.add(layers.Dense(512, activation='relu'))
# print(model.summary()) #depurar camada por camada
model.add(layers.Dense(256, activation='relu', name='my_layer'))
model.add(layers.Dense(10))

# sobreescrevendo o modelo
# = keras.Model(inputs=model.inputs,
                    #outputs=[model.get_layer('my_layer').output]) # (60000, 256)

#model = keras.Model(inputs=model.inputs,
                   # outputs=[model.layers[-1].output]) #(60000, 10)

#feature = model.predict(x_train)
#print(feature.shape)

# = keras.Model(inputs=model.inputs,
                    #outputs=[layer.output for layer in model.layers])

#features = model.predict(x_train)
#for feature in features:
    #(print(feature.shape)
#(60000, 512))
#(60000, 256)
#(60000, 10)

#import sys
#sys.exit()

# Function API (A bit more flexible)
inputs = keras.Input(shape=(784))
x = layers.Dense(512, activation='relu', name='first_layer')(inputs)
x = layers.Dense(25, activation='relu', name='second_layer')(x)
outputs = layers.Dense(10, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

# configurar a parte de treinamento
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(lr=0.001), #taxa de aprendizagem
    metrics=["accuracy"],
)

# mais especificações do treinamento fit
model.fit(x_train, y_train, batch_size=32, epochs=5, verbose=2)

# avaliação após o treinamento
model.evaluate(x_test, y_test, batch_size=32, verbose=2 )


#_________________________________________________________________
#Layer (type)                 Output Shape              Param #
#=================================================================
#input_3 (InputLayer)         [(None, 784)]             0
#_________________________________________________________________
#first_layer (Dense)          (None, 512)               401920
#_________________________________________________________________
#second_layer (Dense)         (None, 25)                12825
#_________________________________________________________________
#dense_6 (Dense)              (None, 10)                260
#=================================================================
#Total params: 415,005
#Trainable params: 415,005
#Non-trainable params: 0
#_________________________________________________________________


#Epoch 1/5
#1875/1875 - 5s - loss: nan - accuracy: 0.0987
#Epoch 2/5
#1875/1875 - 6s - loss: nan - accuracy: 0.0987
#Epoch 3/5
#1875/1875 - 5s - loss: nan - accuracy: 0.0987
#Epoch 4/5
#1875/1875 - 4s - loss: nan - accuracy: 0.0987
#Epoch 5/5
#1875/1875 - 4s - loss: nan - accuracy: 0.0987
#313/313 - 0s - loss: nan - accuracy: 0.0980


# 1. Try and see what accuracy you can get by increasing the model,training for longer
# You should be able to get over 98.1% on the test set!

# 2. Try using different optimizers than Adam, for example Gradient Descent with
# Momentum, Adagrad, and RMSprop

# 3. Is there any difference if you remove the normalization of the data ?
