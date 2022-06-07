# Crie um programa que leia quanto de dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1,00 = R$ 4,70

n = float( input( 'Quanto de dinheiro você tem na carteira? ' ) )
d = float( 4.70 )
print( 'Você pode comprar {:.2f} dolares!'.format( n / d ) )
