'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício 2 - Desafio da videoaula
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c , respectivamente, e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:
esta equação não possui raízes reais
Quando houver apenas uma raiz real imprima:
a raiz desta equação é X
onde X é o valor da raiz
Quando houver duas raízes reais imprima:
as raízes da equação são X e Y
onde X e Y são os valor das raízes.
Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente. Exemplos:
as raízes da equação são 1.0 e 2.0
as raízes da equação são -2.0 e 0.0
'''
import math

a = float(input("Digite o valor do coeficiente quadrático: "))
b = float(input("Digite o valor do coeficiente linear: "))
c = float(input("Digite o valor do termo independente: "))

delta = b**2 - 4*a*c

x1 = (- b + math.sqrt(abs(delta)))/(2*a)

x2 = (- b - math.sqrt(abs(delta)))/(2*a)

if delta > 0:
    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)
    else:
        print("as raízes da equação são", x2, "e", x1)
elif delta == 0:
    print("a raiz desta equação é", x1)
else:
    print("esta equação não possui raízes reais")