# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa

import math

print('=-' * 7, 'DESAFIO 17', '=-' * 7)
cat_op = int(input('Digite o comprimento do cateto oposto: '))
cat_adj = int(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cat_op, cat_adj)
print('A hipotenusa é {:.2f}.'.format(hip))
