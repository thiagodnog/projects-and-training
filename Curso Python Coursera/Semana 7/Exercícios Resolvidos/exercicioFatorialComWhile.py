"""
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Fatorial com repetições encaixadas

Eu quero que você faça programa que vá receber do usuário, que vai digitar uma sequência de números e para cada número que ele digite eu quero que você imprima o fatorial desse número.
"""


entrada = int(input())
while entrada != -1:
    fatorial = 1
    while entrada != 0:
        fatorial = fatorial * entrada
        entrada = entrada - 1
    print(fatorial)
    entrada = int(input())