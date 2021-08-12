""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 7

Escreva uma função chamada é_par(n) que recebe como argumento um inteiro e retorna True se o argumento é um número par e False se ele é ímpar.
"""

def é_par(n):
    par = n % 2 == 0
    return par

numero = int(input("Digite o número a ser avaliado: "))

print(é_par(numero))