'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 5 - Lista de Exercício 4

Exercício 3 - Vogais

Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell do Python:

>> vogal("a")
True
>> vogal("b")
False
>> vogal("E")
True
'''

def vogal(caractere):
    if ((caractere == 'a' or caractere == 'A') or (caractere == 'e' or caractere == 'E') or (caractere == 'i' or caractere == 'I') or (caractere == 'o' or caractere == 'O') or (caractere == 'u' or caractere == 'U')):
        return True
    else:
        return False

vogal('E')