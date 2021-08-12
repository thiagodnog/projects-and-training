'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício Adicional 2 

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:
Digite um numero inteiro: 12345
não

Digite um numero inteiro: 1011
sim
'''

numero = int(input("Digite um numero inteiro: "))

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
        if digitos == 0:
            return print ("não")
        elif (digitoLido == digitoParaLer):
            return print("sim")
        else:
            if quantidadeIteracoes == 1:
                return print("não")
            else:
                quantidadeIteracoes = quantidadeIteracoes - 1       

digitosAdjacentes(numero)