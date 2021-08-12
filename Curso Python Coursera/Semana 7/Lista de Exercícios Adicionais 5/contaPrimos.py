'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Lista de Exercício Adicionais 5

Exercício Adicional 1 - Primos

Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

Exemplo:

>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30

'''

def é_primo(n):
    numeroTestado = 2
    while numeroTestado != 0:

        if n == numeroTestado:
            return 1

        elif n % numeroTestado != 0:
            numeroTestado = numeroTestado + 1

        elif n % numeroTestado == 0:
            return 0


def n_primos(n):
    numero_Testado = 2
    contador = 0

    if n == 2:
        return 1

    while numero_Testado != n:
        contador = contador + é_primo(numero_Testado)
        numero_Testado = numero_Testado + 1
    return (contador)

print(n_primos(121))
