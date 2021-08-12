""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 6

Escreva uma função acheHipot que, dados os comprimento de dois lados de um triângulo retângulo, retorna o comprimento da hipotenusa. 
(Dica: o valor de x ** 0.5 é a raiz quadrada, ou use sqrt do módulo matemático)
"""

def acheHipot(cateto1,cateto2):
    hipotenusa = (cateto1**2 + cateto2**2)**0.5
    return hipotenusa

lado1 = float(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = float(input("Digite o valor do segundo lado do triângulo: "))

print("O valor da hipotenusa é:", acheHipot(lado1,lado2))