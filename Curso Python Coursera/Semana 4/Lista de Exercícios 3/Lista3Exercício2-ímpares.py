"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 4 - Lista de Exercício 3

Exercício 2
Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:

>>Digite o valor de n: 5
1
3
5
7
9

autor: Thiago Nogueira
"""

n = int(input("Digite o valor de n: "))

def impares (inteiro):
    numeroImpar = 0
    numeroPar = 0
    while inteiro != 0:
        numeroImpar = numeroImpar + 1
        if numeroImpar % 2 == 0:
            numeroPar = numeroPar + 1
        else:
            print(numeroImpar)
            inteiro = inteiro - 1

impares(n)



