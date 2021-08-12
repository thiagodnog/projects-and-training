'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 8 - Lista Invertida

Crie um programa que lê uma lista de números terminados em 0 através do teclado e quando o usuário digitar 0 ele imprime a lista ao invertida.
'''



def listaInvertida():
    listaNumeros = []
    numero = 1
    listaNumerosInvertidos = []
    while True:
        numero = int(input())

        if numero != 0:
            listaNumeros.append(numero)

        if numero == 0:
            break
        
    
    for n in range(1,len(listaNumeros)+1):
        listaNumerosInvertidos.append(listaNumeros[-n])
    
    print(listaNumerosInvertidos)

listaInvertida()

