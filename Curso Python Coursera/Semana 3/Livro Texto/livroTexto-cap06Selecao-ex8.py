""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 8

Agora escreva a função é_ímpar(n) que retorna True quando n é ímpar e False caso contrário.
"""

def é_ímpar(n):
    impar = not (n % 2 == 0)
    return impar

numero = int(input("Digite o número a ser avaliado: "))

print(é_ímpar(numero))