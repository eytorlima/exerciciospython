p = float(input('Qual o preço do produto?: '))
mp = int(input("""Qual o método de pagamento?\nPara pagamento à vista no dinheiro/cheque, digite 1.
Para pagamento à vista no cartão, digite 2.
Para pagamento em 2x no cartão, digite 3.
Para pagamento em 3x ou mais no cartão, digite 4: """))

if mp == 1:
    print('Certo. O preço final do produto foi de {:.2f} para {:.2f}.'.format(p, (0.9*p)))

elif mp == 2:
    print('Certo. O preço final do produto foi de {:.2f} para {:.2f}'.format(p, (0.95*p)))

elif mp == 3:
    print('Certo. O preço final do produto é de {:.2f}.'.format(p))

elif mp == 4:
    print('Certo. O preço final do produto é de {:.2f}'.format((p+0.2*p)))

else:
    print('Escolha inválida, favor escolher uma das opções exibidas.')
