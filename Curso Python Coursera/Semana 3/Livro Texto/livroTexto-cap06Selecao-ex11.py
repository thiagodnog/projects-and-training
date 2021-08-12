""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 11

Escreva uma função é_ânguloreto que, dado o comprimento de três lados de um triângulo, determina se o triângulo é retângulo. 
Estenda o programa de forma que os lados possam ser dados à função em qualquer ordem.
"""

def é_ânguloreto (lado1,lado2,lado3):
    if lado1**2 == lado2**2 + lado3**2:
        print(True)
    elif lado2**2 == lado1**2 + lado3**2:
        print(True)
    elif lado3**2 == lado1**2 + lado2**2:
        print(True)
    else:
        print(False)
        

é_ânguloreto(1.5,2,2.5)
