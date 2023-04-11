print('CALCULADORA PESO PEIXES')

p = float(input('Insira o peso do peixe [Kg]: '))
m = 0

if p > 50:
    print('Seu peso excedeu o limite permitido.')
    while p >= 51:
        p = p - 1
        m = m + 4
    while p >= 50.1:
        p = p - 0.1
        m = m + 0.4
    while p >= 50.01:
        p = p - 0.01
        m = m + 0.04

    print(f'Sua multa é de: R${m:.2f}')
    print('Obrigado por utilizar nossos serviços! Volte sempre.')
else:
    print('Obrigado por utilizar nossos serviços! Volte sempre.')
