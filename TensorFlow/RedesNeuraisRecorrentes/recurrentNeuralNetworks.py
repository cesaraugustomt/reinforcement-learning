import tensorflow as tf
import numpy as np
from openpyxl.styles.builtins import output
from tensorflow.keras.datasets import imdb
from tensorflow.python.keras.saving.saved_model.serialized_attributes import metrics

#print(tf.__version__)

# Pré-processamento
# configurando os parâmetros para a base de dados
number_of_words = 20000 #20.000 palavras para todos os textos da base de dados!
max_len = 100 #cada um dos reviews pode ter no máximo 100 palavras

# Carregando a base de dados IMDB
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=number_of_words)
x_train.shape
#print(x_train.shape)
#print(x_train)
#print(x_train[0])
#print(y_train)

# Preenchimento das sequências (textos) para terem o mesmo tamanho
#print(len(x_train[0])) #218
#print(len(x_train[1])) #189
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_len)
#print(len(x_train[0])) #100
#print(len(x_train[1])) #100
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=max_len)

# Construindo a Rede Neural Recorrente
model = tf.keras.Sequential()
# Adicionando a camada de (embedding)
# https://www.tensorflow.org/tutorials/text/word_embeddings?hl=pt-br
# vamos passar sentença que tenha no máximo 100 palavras -> input_shape=(x_train.shape[1]
model.add(tf.keras.layers.Embedding(input_dim=number_of_words, output_dim=128, input_shape=(x_train.shape[1],)))
# Adicionando a camada LSTM -> células de memória (units=128)
model.add(tf.keras.layers.LSTM(units=128, activation='tanh'))
# Adicionando a camada de saída
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))


# Compilando o modelo
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
#print(model.summary())

# Treinando o modelo
model.fit(x_train, y_train, epochs=3, batch_size=128)

# Avaliando o modelo
test_loss, test_acurracy = model.evaluate(x_test, y_test)
print("Test accuracy: {}".format(test_acurracy))
print("Test loss: {}".format(test_loss))