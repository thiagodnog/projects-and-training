"""
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Decomposição em fatores primos com repetições encaixadas

Dado número inteiro n, sendo que n é maior que 1, positivo maior que 1 imprimir a sua decomposição fatores primos indicando também a multiplicidade de cada fator.
"""

n = int(input("Digite um número inteiro >1: "))

fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print("fator", fator, "multiplicdade = ", multiplicidade)
    fator = fator + 1
    multiplicidade = 0