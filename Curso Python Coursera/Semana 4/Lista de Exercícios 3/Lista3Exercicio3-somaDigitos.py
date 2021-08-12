"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 4 - Lista de Exercício 3

Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

>>Digite um número inteiro: 123
6

autor: Thiago Nogueira
"""
n = int(input("Digite um número inteiro: "))

def somaDigitos(digitos):
    digitosParaSomar = digitos % 10
    digitosRestantes = digitos // 10
    digitosSomados = 0
    quantidadeIteracoes = len(str(digitos))
    while (quantidadeIteracoes != 0):
        digitosSomados = digitosSomados + digitosParaSomar
        digitosParaSomar = digitosRestantes % 10
        digitosRestantes = digitosRestantes // 10
        quantidadeIteracoes = quantidadeIteracoes - 1
    
    return print(digitosSomados)

somaDigitos(n)