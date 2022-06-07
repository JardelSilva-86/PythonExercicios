# Crie um progrma que converta a temperatura digitada em ºC para a temperatura em ºF

print('=-'*7, 'DESAFIO 9', '=-'*7)
cel = float(input("Digite a temperatura em ºC: "))
fahre = ((9 * cel) / 5) + 32
print("A temperatura de {}ºC corresponde a {}ºF".format(cel,fahre))
