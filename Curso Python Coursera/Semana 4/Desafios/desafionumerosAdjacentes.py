"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 4 - Desafio

Dado um número, escrever um programa para verificar se há dois dígitos iguais adjacentes. Ex:

funcaoQualquer(123456) # retorna False
funcaoQualquer(4566897907) # retorna True
funcaoQualquer(44) # retorna True

autor: Thiago Nogueira
"""

numero = int(input("Digite o número a ser verificado: "))

def digitosAdjacentes(digitos):
    digitoParaLer = digitos % 10
    digitosRestantes = digitos // 10
    digitoLido = 0
    quantidadeDigitos = len(str(digitos))
    quantidadeIteracoes = quantidadeDigitos
    
    while (quantidadeIteracoes != 0):
        digitoLido = digitoParaLer
        digitoParaLer = digitosRestantes % 10
        digitosRestantes = digitosRestantes // 10
        if (digitoLido == digitoParaLer):
            return print(True)
        else:
            if quantidadeIteracoes == 1:
                return print(False)
            else:
                quantidadeIteracoes = quantidadeIteracoes - 1       

digitosAdjacentes(numero)