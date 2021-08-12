"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 5 - Desafio

Escreva um programa para encontrar as raízes de uma função de segundo grau con funções em python. 

autor: Thiago Nogueira
"""

a = int(input("Digite o valor do coeficiente quadrático: "))
b = int(input("Digite o valor do coeficiente linear: "))
c = int(input("Digite o valor do termo independente: "))



def Delta(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def raizes(a,b):
    delta = Delta(a,b,c)
    x1 = (- b + delta**(1/2)) / 2*a
    x2 = (- b - delta**(1/2)) / 2*a

    if delta > 0:
        print("As raizes da equação são:", "x1 =", x1, "e x2 =", x2)
    elif delta == 0:
        print("A raiz da equação é x =", x1)
    else:
        print("Não há raiz real.")

raizes(b,c)