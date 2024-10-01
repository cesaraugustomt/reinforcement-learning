# Intuição Deep Q-Learning - Aprendizagem

O Q-Learning clássico ele em geral vai ser executado com sucesso em ambiente
mais simples e ele não vai funcionar muito bem em ambiente mais complexos com
por exemplo em carro autônomos ou então com jogos. Para trabalhar com problemas
mais complexos precisamos usar o **Deep Q-Learning** utilizando redes neurais.

![alt text](../imagens/AprendizadoPorReforco/deep.png)

O que acontece agora para a previsão do **Q** da ação é que ele compara a previsão
da rede neural com o valor da previsão anterior.

Nós precisamos também calcular a função de **loss function** que é a função de
erro nessa função ele pega o **Q-Target** que é os valores anteriores que nós
tinhamos e fazemos a subtração com os valores de **Q** que são as previsões da
rede neural e elevamos ao quadrado que é o cálculo de **mean squared error**.
Então após feito o somátorio pegamos esse valor e passamos para o inicio da rede
neural, e ele ira executar por *x* épocas até que ele consiga aproximar esses
valores de *Q*.

observação: nos métodos passados precisavamos que o *antés* precisaria ser muito
próximo do *depois* por meio daquela fórmula da diferença temporal e aqui nós 
temos um conceito bem parecido, o que vai mudar é que nós vamos comparar as 
respostas que nós tinhamos antés com as previsões das redes neurais e nós temos
o adicional que é o uso da *loss function* para nós fazermos essas repetições e
esses ajustes dos pesos. E na próxima vez que o agente estiver andando pelo 
ambiente ele já vai ter acesso aos pesos da rede neural o que vai mudar em qual
ação o agente deve tomar. 

![alt text](../imagens/AprendizadoPorReforco/deep1.png)