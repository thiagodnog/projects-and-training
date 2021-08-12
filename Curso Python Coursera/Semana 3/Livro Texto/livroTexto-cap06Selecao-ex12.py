""""
Curso de Introdução à Ciência da Computação com Python Parte 1

Livro Texto 

Exercício 12

Um ano é bissexto se ele é divisível por 4 a menos que seja um século que não é divisível por 400 ou é divisível por 100. 
Escreva uma função que receba um ano como argumento e retorna True se o ano é bissexto e False caso contrário.
"""

def éBissexto(ano):
    if ano < 400:
        if ano % 4 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        if ano % 4 == 0:
            if ano % 100 == 0:
                bissexto = False
            else:
                bissexto = True
        else:
            if ano % 400 == 0:
                bissexto = True
            else:
                bissexto = False
    return bissexto

print(éBissexto(1900))
        

        

