t1 = int(input('Escreva o primeiro termo da PA: '))
r = int(input('Escreva a razão da PA: '))
n = 1
for c in range(1, 11):
    print('O termo {} da PA é {}.'.format(n, t1))
    n = n+1
    t1 = t1+r
