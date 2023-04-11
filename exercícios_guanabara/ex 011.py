l = float(input('Insira, em metros, a largura da parede que desejas pintar: '))
a = float(input('Insira, em metros, a altura da parede que desejas pintar: '))
aa = l*a

print('Sua parede possui uma área de {} metros quadrados e precisará, portanto, de {} litros de tinta (cada litro pinta 2m²)'.format(aa, aa/2))
