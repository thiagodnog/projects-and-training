""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 10

Escreva uma função é_ânguloreto que, dado o comprimento de três lados de um triângulo, determina se o triângulo é retângulo. 
Asssuma que o terceiro argumento é sempre o lado maior. Ela retorna True se é um triângulo retângulo, ou False caso contrário.
"""

def é_ânguloreto (lado1,lado2,lado3):
    return print(lado3**2 == lado1**2 + lado2**2)

é_ânguloreto(4,8,16)