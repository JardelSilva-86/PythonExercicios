# Crie um programa que peça 2 motas ao usuário e retorne a média destas notas.

print('=-' * 7, 'DESAFIO 6', '=-' * 7)
a = input('Nome do Aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média do aluno(a) {} foi de {:.2f}.'.format(a, m))