"""
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Lista de Exercício 5

Exercício 1 

Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
##########
##########

digite a largura: 2
digite a altura: 2
##
##
"""
largura = int(input("digite a lagura: "))
altura = int(input("digite a lagura: "))
contador = largura

while altura != 0:
    while contador != 0:
        print("#", end="")
        contador = contador - 1
    altura = altura - 1
    print()
    contador = largura
