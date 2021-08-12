"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 4 - Lista de Exercício 3

Exercício 1
Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

Exemplo:

>>Digite o valor de n: 5
120

autor: Thiago Nogueira
"""
n = int(input("Digite o valor de n: "))

def fatorial (numero):
    fatorial = numero
    if numero == 0:
        return print(1)
    else:
        while numero > 1 :
            fatorial = fatorial * (numero - 1)
            numero = numero - 1
        return print(fatorial)

fatorial(n)
