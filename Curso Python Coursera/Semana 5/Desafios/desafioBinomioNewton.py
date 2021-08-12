"""
Curso - Introdução à Ciência da Computação com Python Parte 1

Semana 5 - Desafio

Escreva um programa utilizando funções para calcular um binômio de Newton através dos coeficientes binomiais. 

Exemplo:

>>Digite o valor de n: 5
120

autor: Thiago Nogueira
"""
#n = int(input("Digite o valor do número de combinações n: "))
#k = int(input("Digite o termo k: "))

def binomio (n,k):
    binomial = 0
    if k > n:
        print ("Erro! o a relação k < = n deve ser verdadeira")
    else:
        binomial = fatorial(n) / (fatorial(k)*fatorial(n-k))
        return binomial


def fatorial (numero):
    fatorial = numero
    if numero == 0:
        return 1
    else:
        while numero > 1 :
            fatorial = fatorial * (numero - 1)
            numero = numero - 1
        return fatorial

#binomio(n,k)