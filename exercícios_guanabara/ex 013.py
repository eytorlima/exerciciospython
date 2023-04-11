s = float(input('Insira o valor do seu salário para receber um reajuste de 15% de aumento: R$'))
sn = s+((15/100)*s)

print('Pronto! Seu salário passou de R${} para R${:.2f} !'.format(s, sn))
