'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 5 - Lista de Exercício 4

Exercício 1 - Máximo

Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Exemplos de execução no shell do Python:

>> maximo(3, 4)
4
>> maximo(0, -1)
0
'''

def maximo(num1,num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

maximo(3,4)
