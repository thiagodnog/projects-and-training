'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício Adicional 1 - FizzBuzz 

Reescreva a função 'maximo' do outro exercício, que devolve o maior valor dentre dois inteiros recebidos, para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.

Exemplos de execução no Python Shell:
>>>maximo(30, 14, 10)
30
>>>maximo(0, -1, 1)
1
'''

def maximo(num1,num2,num3):
    if num1 > num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3


