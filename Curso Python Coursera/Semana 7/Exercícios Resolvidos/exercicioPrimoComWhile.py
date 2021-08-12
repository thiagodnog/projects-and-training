"""
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Números Primos com repetições encaixadas

Dado número inteiro n, sendo que n é maior que 1, positivo maior que 1 imprimir a sua decomposição fatores primos indicando também a multiplicidade de cada fator.
"""

n = int(input())
numeroTestado = 2

while numeroTestado != 0:

    if n == numeroTestado:
        print("É PRIMO")
        numeroTestado = 0

    elif n % numeroTestado != 0:
        numeroTestado = numeroTestado + 1

    elif n % numeroTestado == 0:
        print("NÃO É PRIMO")
        numeroTestado = 0


    