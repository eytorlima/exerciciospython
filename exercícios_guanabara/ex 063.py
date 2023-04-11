print('Fibonacci')

n = int(input('Quantas linhas da sequência você quer ver?: '))
t1 = 0
t2 = 1
t3 = t1+t2
c = 3

if n > 2:
    print('{} -> {} -> '.format(t1, t2), end='')

    while c <= n:
        print('{} -> '.format(t3), end='')
        t1 = t2
        t2 = t3
        t3 = t1+t2
        c = c+1

    print('FIM')

if n == 2:
    print('{} -> {} -> '.format(t1, t2), end='')
    print('FIM')

if n == 1:
    print('{} -> '.format(t1), end='')
    print('FIM')

if n == 0:
    print('FIM')
