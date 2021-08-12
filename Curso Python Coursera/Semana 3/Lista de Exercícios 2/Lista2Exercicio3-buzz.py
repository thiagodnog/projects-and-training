"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Exercícios 3 - FizzBuzz parcial, parte 2

Receba um número inteiro na entrada e imprima
Buzz
se o número for divisível por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

autor: Thiago Nogueira
"""

numInt = int(input("Digite um número inteiro: "))

if numInt % 5 == 0:
    print("Buzz");
else:
    print(numInt);