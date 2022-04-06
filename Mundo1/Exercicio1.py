### Crie um programa que leia o nome da pessoa e mostre uma msg de boas vindas.

print('=-' *7, 'DESAFIO 2', '=-'*7)
dia = int(input('Qual o dia de seu nascimento? '))
mes = int(input('Qual o mês do seu nascimento? '))
ano = int(input('Qual é o ano do seu nascimento? '))
print('Você nasceu no dia {:2} de {} de {}, correto?'.format(dia, mes, ano))