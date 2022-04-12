# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

print('=-'*7, 'DESAFIO 11', '=-'*7)
metro = float(input("Digite um distância em metros: "))
print("A conversão da distância {} metros é equivalente a: ".format(metro))
print("{:.2f} em Quilometros (km).".format(metro / 1000))
print("{:.2f} em Hectometros (hm).".format(metro / 100))
print("{:.2f} em Decâmetro (dam).".format(metro / 10))
print("{:.0f} em Decimetro (dm).".format(metro * 10))
print("{:.0f} em Centímetro (cm).".format(metro * 100))
print("{:.0f} em Milímetro (mm).".format(metro * 1000))