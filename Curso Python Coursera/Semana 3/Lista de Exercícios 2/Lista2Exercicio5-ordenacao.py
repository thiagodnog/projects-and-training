"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima
crescente
se eles forem dados em ordem crescente. Caso contrário, imprima
não está em ordem crescente

autor: Thiago Nogueira
"""

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))

if num1<num2<num3:
    print("crescente")
else:
    print("não está em ordem crescente")