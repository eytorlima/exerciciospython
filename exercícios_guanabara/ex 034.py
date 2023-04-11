s = float(input('Insira o seu salário: R$'))
if s > 1250:
    print('Seu salário passou de {:.2f} para {:.2f}'.format(s, s+(0.1*s)))

else:
    print('Seu salário passou de {:.2f} para {:.2f}'.format(s, s+(0.15*s)))
