print('Tabuada\n')

while True:
    n = int(input('Insira um número para obter sua tabuada: '))

    if n < 0:
        break
    print(f'{n}x1={n * 1}; {n}x2={n * 2}; {n}x3={n * 3}; {n}x4={n * 4}; {n}x5={n * 5};')
    print(f'{n}x6={n * 6}; {n}x7={n * 7}; {n}x8={n * 8}; {n}x9={n * 9}; {n}x10={n * 10}.')
    print('')

print('FIM')