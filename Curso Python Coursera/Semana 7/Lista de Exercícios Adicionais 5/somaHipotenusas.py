'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Semana 7 - Lista de Exercício Adicionais 5

Exercício Adicional 2 - (Difícil) Soma das hipotenusas

Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras, n é uma hipotenusa se existem números inteiros i e j tais que:

n^2 = i^2 + j^2n 
 
Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço de 1 até nn testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

Exemplo:
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105
'''
def soma_hipotenusas(N):
    n = 1
    i = 1
    j = 1
    soma = 0
    while n != 0:
        while j != 0:
            while i != 0:
                if n**2 == i**2 + j**2:
                    soma = soma + n
                    break

                elif i < n:
                    i = i + 1

                elif i == n:
                    i = 1
                    break

            if n**2 == i**2 + j**2:
                    soma = soma + n
                    break

            elif j < n:
                i = i + 1

            elif j == n:
                j = 1
                break
            j = j + 1
        
        if n == N:
            break
        n = n + 1

    soma = soma//2
    return soma

print(soma_hipotenusas(25))