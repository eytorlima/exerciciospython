import time

t1 = int(input('Digite o termo 1 da PA: '))
razao = int(input('Digite a razão da PA: '))
n = 1
c = 0
time.sleep(0.25)

while c != 10:
    print('O {}º termo da PA é {}.'.format(n, t1))
    n = n+1
    c = c+1
    t1 = t1+razao

a = str(input('\nDeseja ver mais alguns termos dessa PA?[S/N]: ')).strip().title()[0]

if a == 'S':
    a2 = int(input('\nQuantos termos você deseja ver?: '))

    while a2 > 0:
        a2 = a2-1
        print('O {}º termo da PA é {}.'.format(n, t1))
        n = n+1
        c = c+1
        t1 = t1+razao

    if a2 == 0:
        print('\nPrograma encerrado.')

else:
    print('\nPrograma encerrado.')
