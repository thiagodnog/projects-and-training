'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício Adicional 1 

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:
Digite um numero inteiro: 13
primo

Digite um numero inteiro: 12
não primo
'''

n = int(input("Digite um numro inteiro: "))

def primalidade(numero):
    if (numero % 2 == 0) or (numero % 3 == 0) or (numero % 5 == 0) or (numero % 7 == 0):
        if numero == 5 or numero == 7:
            return print("primo")
        else:
            return print("não primo")
    else:
        return print("primo")

primalidade(n)