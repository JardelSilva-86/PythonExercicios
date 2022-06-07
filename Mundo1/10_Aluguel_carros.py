# Crie um programa que pergunte ao usuário a quantidade de KM percorridos por um carro alugado. Pergunte quantos dias esse carro foi alugado. Calcule o preço total a pagar pelo aluguel. Considerando a diária custa R$ 60 e o KM rodado custa R$ 0,15.

print('=-'*7, 'DESAFIO 10', '=-'*7)
diaria = 60
custo_km = 0.15
dia_alug = int(input("Quantos dias o carro será alugado? "))
km_perc = int(input("Quantos KM o carro percorreu? "))
valor_alug = dia_alug * diaria
valor_km = km_perc * custo_km

print("O carro será alugado por {} dias,isso custará R$ {:.2f} no total.".format(dia_alug, valor_alug))
print("A quantidade de KM rodados foi de {} km e isso custará R$ {:.2f} no total.".format(km_perc, valor_km))
print("O valor total a ser pago será de R$ {:.2f}.".format(valor_km + valor_alug))
