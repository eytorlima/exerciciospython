n = int(input('Insira um número qualquer para obter seu fatorial: '))
i = 2
fat = 1

if n == 0:
    print('0! é 1.')

while n >= i:
    fat = fat*i
    i = i+1

print('{}! é igual a {}.'.format(n, fat))
