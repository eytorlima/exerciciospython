d = float(input('Insira a distância da viagem em KM: '))
if d <= 200:
    p = d*0.5
    print('O preço da viagem é de R${:.2f}.'.format(p))

else:
    p1 = d*0.45
    print('O preço da viagem é de R${:.2f}'.format(p1))
