'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício Adicional 1 - FizzBuzz 

Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Exemplos de execução no Python Shell:
>>>fizzbuzz(3)
"Fizz"
>>>fizzbuzz(5)
"Buzz"
>>>fizzbuzz(15)
"FizzBuzz"
>>>fizzbuzz(4)
4
'''

def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return 'Fizz'
    elif numero % 5 == 0 and numero % 3 != 0:
        return 'Buzz'
    elif numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    elif numero % 5 != 0 and numero % 3 != 0:
        return numero


