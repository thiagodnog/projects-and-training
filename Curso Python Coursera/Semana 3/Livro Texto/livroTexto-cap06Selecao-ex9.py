""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 9

Modifique é_ímpar de forma que ela use uma chamada para é_par para determinar se o argumento é um inteiro par ou ímpar.
"""

numero = int(input("Digite o número a ser avaliado: "))

def é_par(n):
    par = n % 2 == 0
    return par

def é_ímpar(n):
    if é_par(numero) == True:
        num="inteiro par"
    else:
        num="ímpar"
    return num

print(é_ímpar(numero))
