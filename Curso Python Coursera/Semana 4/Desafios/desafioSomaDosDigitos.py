"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 4 - Desafio

Dado um número, escrever um programa para que seja retornado a soma dos dígitos desse número. Ex:

funcaoQualquer(123) # retorna 6
funcaoQualquer(456) # retorna 15
funcaoQualquer(44) # retorna 8

autor: Thiago Nogueira
"""
numero = int(input("Digite o número que terá os dígitos somados: "))

def somaDigitos(digitos):
    digitosParaSomar = digitos % 10
    digitosRestantes = digitos // 10
    digitosSomados = 0
    while (digitosParaSomar != 0):
        digitosSomados = digitosSomados + digitosParaSomar
        digitosParaSomar = digitosRestantes % 10
        digitosRestantes = digitosRestantes // 10
    
    return print(digitosSomados)

somaDigitos(numero)
        


