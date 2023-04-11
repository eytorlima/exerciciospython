vc = float(input('Qual o valor da casa desejada?: '))
sa = float(input('Qual o valor do salário do comprador?: '))
y = int(input('Em quantos anos pretende pagar?: '))

vpm = float(vc / (y * 12))

if vpm > (0.3*sa):
    print('Você não poderá comprar a casa.')

else:
    print('Parabéns, sua compra foi aprovada, o custo da prestação mensal é de R${:.3f}.'.format(vpm))
