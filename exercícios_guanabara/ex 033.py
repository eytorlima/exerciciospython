n1 = float(input('Insira um número real qualquer: '))
n2 = float(input('Insira outro número real qualquer: '))
n3 = float(input('Insira um último número real qualquer: '))

if n1>n2>n3:
    print(f'{n1}>{n2}>{n3}.')

if n1>n3>n2:
    print(f'{n1}>{n3}>{n2}.')

if n2>n1>n3:
    print(f'{n2}>{n1}>{n3}.')

if n2>n3>n1:
    print(f'{n2}>{n3}>{n1}.')

if n3>n1>n2:
    print(f'{n3}>{n1}>{n2}')

if n3>n2>n1:
    print(f'{n3}>{n2}>{n1}')
