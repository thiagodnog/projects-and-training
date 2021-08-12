'''
Curso de Introdução à Ciência da Computação com Python Parte 1

Exercício 1 - Distância entre dois pontos
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
longe
na saída. Caso o contrário, quando a distância for menor que 10, imprima
perto
'''
import math

x1 = int(input("Digite o valor da coordenada x do primeiro número: "))
y1 = int(input("Digite o valor da coordenada y do primeiro número: "))
x2 = int(input("Digite o valor da coordenada x do segundo número: "))
y2 = int(input("Digite o valor da coordenada x do segundo número: "))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if distancia > 10:
    print("longe")
else:
    print("perto")

