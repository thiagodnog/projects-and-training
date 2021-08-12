"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 3 - Lista de Exercício 2

Exercício 1 - Par ou ímpar?
Receba um número inteiro na entrada e imprima
par
quando o número for par ou
ímpar
quando o número for ímpar.

autor: Thiago Nogueira
"""

numInt = int(input("Digite um número inteiro: "))

if numInt % 2 == 0:
    print("par");
else:
    print("ímpar");

