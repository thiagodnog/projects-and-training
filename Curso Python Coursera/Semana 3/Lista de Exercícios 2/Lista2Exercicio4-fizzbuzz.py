"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Exercícios 4 - FizzBuzz parcial, parte 3
Receba um número inteiro na entrada e imprima
FizzBuzz
na saída se o número for divisível por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

autor: Thiago Nogueira
"""

numInt = int(input("Digite um número inteiro: "))

if numInt % 3 == 0 and numInt % 5 == 0:
    print("FizzBuzz");
else:
    print(numInt);