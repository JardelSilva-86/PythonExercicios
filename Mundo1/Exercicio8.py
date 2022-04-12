''' Crie um programa que leia a largura e a altura de uma parde em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 m² de parede.'''

print('=-'*7, 'DESAFIO 8', '=-'*7)
largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
tinta = area / 2
print("A sua parede tem dimensões {:.1f}x{:.1f} e a área total é de {:.3f}m.".format(largura, altura, area))
print("Será necessário {:.1f}l de tinta para pintar a parede.".format(tinta))
