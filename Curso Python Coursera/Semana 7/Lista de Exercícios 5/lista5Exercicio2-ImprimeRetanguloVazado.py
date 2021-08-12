"""
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Lista de Exercício 5

Exercício 2

Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##
"""

largura = int(input("digite a lagura: "))
altura = int(input("digite a lagura: "))
contadorLargura = largura
contadorAltura = altura

while contadorAltura != 0:
    while contadorLargura != 0:
        if contadorAltura == 1 or  contadorAltura == altura: 
            print("#", end="")
            contadorLargura = contadorLargura - 1

        else:
            if contadorLargura == 1 or contadorLargura == largura:
                print("#",end="")
                contadorLargura = contadorLargura - 1
            else:
                print(" ",end="")
                contadorLargura = contadorLargura - 1
    contadorAltura = contadorAltura - 1
    print()
    contadorLargura = largura