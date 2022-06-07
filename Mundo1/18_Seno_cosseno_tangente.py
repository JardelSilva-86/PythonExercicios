# Faça um programa que leia um ângulo e mostre na tela o valor do seno, cosseno e tangente

print('=-'*7, 'DESAFIO 18', '=-'*7)
import math
ang = int(input('Digite o valor de um ângulo: '))
print('O ângulo {} tem as seguintes características: '.format(ang))
print('O valor do seno é {:.2}.'.format(math.sin(ang)))
print('O valor do cosseno é {:.2f}.'.format(math.cos(ang)))
print('O valor da tangente é {:.2f}.'.format(math.tan(ang)))
