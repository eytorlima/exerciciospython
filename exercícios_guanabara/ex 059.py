import time

n1 = float(input('Digite o primeiro número: '))
time.sleep(0.15)
n2 = float(input('Digite o segundo número: '))
time.sleep(0.25)
o = int(input("""\n[1] Somar.
[2] Multiplicar.
[3] Maior valor.
[4] Novos números.
[5] Sair do programa.\n
Qual operação você deseja realizar?: """))
time.sleep(0.25)
if o != 4:
    if o == 1:
        print('A soma de {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, (n1+n2)))
    if o == 2:
        print('A multiplicação de {:.2f} por {:.2f} é {:.2f}.'.format(n1, n2, (n1*n2)))
    if o == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        if n2 > n1:
            print('O maior número é {}.'.format(n2))
        if n1 == n2:
            print('{} é igual a {}.'.format(n1, n2))
    if o == 5:
        print('Ok. Saindo do programa...')

while o == 4:
    print('Ok... insira novos números.')
    time.sleep(0.15)
    n1 = float(input('Digite o primeiro número: '))
    time.sleep(0.15)
    n2 = float(input('Digite o segundo número: '))
    time.sleep(0.25)
    o = int(input("""\n[1] Somar.
[2] Multiplicar.
[3] Maior valor.
[4] Novos números.
[5] Sair do programa.\n
Qual operação você deseja realizar?: """))
    time.sleep(0.15)
    if o == 1:
        print('A soma de {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, (n1+n2)))
    if o == 2:
        print('A multiplicação de {:.2f} por {:.2f} é {:.2f}.'.format(n1, n2, (n1*n2)))
    if o == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        if n2 > n1:
            print('O maior número é {}.'.format(n2))
        if n1 == n2:
            print('{} é igual a {}.'.format(n1, n2))
    if o == 5:
        print('Ok. Saindo do programa...')
