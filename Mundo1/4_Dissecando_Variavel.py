# Crie um programa que leia algo e mostre seu tipo pimitivo e todas as informações possíveis sobre ele.

print('=-'*7, 'DESAFIO 4', '=-'*7)
n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(n))) # Ponto de melhoria!
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('É alfabético? {}'.format(n.isalpha()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está capitalizada? {}'.format(n.istitle()))
