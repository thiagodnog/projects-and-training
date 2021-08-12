'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 5 - Lista de Exercício 4

Exercício 2 - Primos

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplo:

>> maior_primo(100)
97
>> maior_primo(7)
7
'''

def maior_primo(numero):
    condicaoDeParada = False
    while (condicaoDeParada == False):
        testaNumero = primo(numero)
        if (testaNumero == True):
            condicaoDeParada = True
            return numero
        else:
            numero = numero - 1        


def primo(numero):
    if (numero % 2 == 0) or (numero % 3 == 0) or (numero % 5 == 0) or (numero % 7 == 0) or (numero % 31 == 0):
        if numero == 5 or numero == 7 or numero == 31:
            return True
    else:
        return True

print(maior_primo(31))