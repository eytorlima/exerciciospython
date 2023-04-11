n = int(input('Insira um número inteiro qualquer para obter sua tabuada: '))
a = 0
for c in range(0, 11):
    print('{}x{} = {}.'.format(n, a, n*a))
    a = a+1
