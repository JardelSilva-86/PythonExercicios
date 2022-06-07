# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteiro

print( '=-'*7, 'DESAFIO 16', '=-'*7 )
from math import trunc
n = float( input( 'Digite um número decimal: ') )
print( trunc( n ) )
