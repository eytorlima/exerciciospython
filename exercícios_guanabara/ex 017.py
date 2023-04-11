import math
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

print('O valor da hip desse triângulo retângulo é: {:.2f}'.format(math.sqrt(ca**2+co**2)))
