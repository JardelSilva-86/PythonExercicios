# PythonExercicios
## Exercicios de Python_Mundo1

### Crie um programa que leia o nome da pessoa e mostre uma msg de boas vindas.
print('=' * 7 DESAFIO 1 '=' * 7)
nome = input('Qual é o seu nome? ')
print('Olá ,{}! É um prazer te conhecer!'.format(nome))

### Crie um programa que solicite a data de nascimento de uma pessoa.
print('=' * 7 DESAFIO 2 '=' * 7)
dia = int(input('Qual é o dia do seu nascimento? '))
mes = str(input('Qual é o nome do mês do seu nascimento? '))
ano = int(input('Qual é o ano do seu nascimento? '))
print('Você nasceu no dia {} de {} de {}, correto?'.format(dia, mes, ano))

### Crie um programa que some 2 números
print('=' * 7 DESAFIO 3 '=' * 7)
primeiroNum = input('Primeiro número: ')
segundoNum = input('Segundo número: ')
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

### Crie um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada
print('=' * 7 DESAFIO 5 '=' * 7)
n = int(input('Digite um número: '))
print('Analisando o número {}, seu antecessor é {} e seu sucessor é {}  '.format(n, n - 1, n + 2))

### Crie um programa que solicite um número ao usúario e mostre o dobro, triplo e raiz quadrada. 
print('===== DESAFIO 6 =====')
n1 = int(input('Digite um número: '))
print('O número é: {}'.format(n1))
print('O dobro é: {}'.format(n1 * 2))
print('O triplo é: {}'.format(n1 * 3))
print('A raiz quadrada é: {:.2f}'.format(n1 ** (1/2)))