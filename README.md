# PythonExercicios
## Exercicios de Python_Mundo1

### Crie um programa que leia o nome da pessoa e mostre uma msg de boas vindas.
print('===== DESAFIO 1 =====')
nome = input('Qual é o seu nome? ')
print('Olá ,{}! É um prazer te conhecer!'.format(nome))

### Crie um programa que solicite a data de nascimento de uma pessoa.
print('===== DESAFIO 2 =====')
dia = int(input('Qual é o dia do seu nascimento? '))
mes = str(input('Qual é o nome do mês do seu nascimento? '))
ano = int(input('Qual é o ano do seu nascimento? '))
print('Você nasceu no dia {} de {} de {}, correto?'.format(dia, mes, ano))

### Crie um programa que some 2 números
print('===== DESAFIO 3 =====')
primeiroNum = input('Primeiro número =')
segundoNum = input('Segundo número =')
soma = int(primeiroNum) + int(segundoNum)
print('A soma é {}.'.format(soma))

### Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
print('=' * 7 DESAFIO 4 '=' * 7)
n1 = input('Digite algo = ')
print('O tipo primitivo desse valor é {}'.format(type(n1)))
print('So tem espaço? {}'.format(n1.isspace()))
print('É um número? {}'.format(n1.isnumeric()))
print('É alfanumérico? {}'.format(n1.isalnum()))
print('É alfabético? {}'.format(n1.isalpha()))
print('Está em minúsculas? {}'.format(n1.islower()))
print('Está em maiúsculas? {}'.format(n1.isupper()))
print('Está capitalizada? {}'.format(n1.istitle()))
