"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 3 - Desafio

Escreva um programa para encontrar as raízes de uma função de segundo grau. 

autor: Thiago Nogueira
"""

import math

a = int(input("Digite o valor do coeficiente quadrático: "))
b = int(input("Digite o valor do coeficiente linear: "))
c = int(input("Digite o valor do termo independente: "))

delta = b**2 - 4*a*c

x1 = (- b + math.sqrt(abs(delta)))/(2*a)

x2 = (- b - math.sqrt(abs(delta)))/(2*a)

if delta > 0:
    print("As raizes da equação são:", "x1 =", x1, "e x2 =", x2)
elif delta == 0:
    print("A raiz da equação é x =", x1)
else:
    print("Não há raiz real.")