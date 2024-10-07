# Tensor Basics
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# Fazer o tensorflow não alocar toda a memória na gpu
# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Initialization of Tensors
x = tf.constant(4, shape=(1,1), dtype=tf.float32) # criando uma matriz 1x1
x = tf.constant([[1,2,3], [4,5,6]]) # criando uma matriz bidimensional 2x2

x = tf.ones((3,3)) #obtendo uma matriz tridimensional 3x3
x = tf.zeros((2, 3)) # matriz 2x3
x = tf.eye(3) #matriz na diagonal 3x3 I for the identity matrix (eye)

x = tf.random.normal((3,3), mean=0, stddev=1) # para ter uma distribuição uniforme
x = tf.random.uniform((1,3), minval=0, maxval=1) # ter pontos aleatórios uniforme
x = tf.range(9) #obtemos um array de 9
x = tf.range(start=1, limit=10, delta=2)

x.cast(x, dtype=tf.float64) # cast é uma maneira de converter entre os tipos d
# tf.float (16,32,64), tf.int (8,16,32,64), tf.bool


# Mathematical Operations
x = tf.constant([1,2,3])
y = tf.constant([9,8,7])

z = tf.add(x, y) #soma
z = x + y

z = tf.subtract(x, y) #subtração
z = x - y

z = tf.divide(x, y) #divisão
z = x / y

z = tf.multiply(x, y) #multiplicação
z = x * y

z = tf.tensordot(x, y, axes=1) #obter o produto
z = tf.reduce_sum(x*y, axis=0)

z = x ** 5 #exponenciação

x = tf.random.normal((2, 3))
y = tf.random.normal((3, 4))
z = tf.matmul(x, y) #fazer um mat na multiplicação
z = x @ y


# Indexing
x = tf.constant([0,1,1,2,3,1,2,3])
print(x[:]) #imprimir todos os elementos
print(x[1:]) #excluir o primeiro elemento
print(x[1:3]) #excluir o 1 e mostra somente os 3 primeiros
print(x[::2]) #pula de 1 em 1 elemento
print(x[::-1]) #imprimir em ordem inversa


# especificando os índices
indices = tf.constant([0,3])
x_ind = tf.gather(x, indices)
print(x_ind)

indices = tf.constant([[0,3],
                       [3,4],
                       [5.6]])

print(x[0,:]) #deve pegar a primeira coluna
print(x[0:2,:])


# Reshaping
x = tf.range(9) #gera 9 elementos
print(x)

x = tf.reshape(x, (3,3)) #podemos remodelar esses elementos em uma matriz
print(x)

x = tf.transpose(x, perm=[1,0]) #transposição e permutação
print(x)