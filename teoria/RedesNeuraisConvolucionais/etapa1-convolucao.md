# Etapa 1 - Operador de convolução

- Convolução é o processo de adicionar cada elemento da imagem
  para seus vizinhos, ponderado por um kernel: Cálculos e soma de
  matrizes para fazermos alteração de determinados pixels da imagem
  que é ponderado por um kernel.

- A imagem é uma matriz e o kernel é outra matriz.

![alt text](../imagens/RedesNeuraisConvolucionais/etapa1.png)

## Links

- Explicações sobre os kernels
  [wikipedia Kernel_image_processing ](<https://en.wikipedia.org/wiki/Kernel_(image_processing)>)

- Exemplo on-line [setosa image-kernels](https://setosa.io/ev/image-kernels/)

A ideia de trabalhar com o pré processamento em uma rede convolucional é
na primeira etapa pegar a imagem original e fazer a aplicação desses tipos
de kernels para ele fazer a modificação na imagem e começar a eliminar
características que não são essenciais para o treinamento.
