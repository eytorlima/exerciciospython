numeros = (int(input('Digite o último número: ')), int(input('Digite um número: ')),
           int(input('Digite outro número: ')), int(input('Digite mais um número: ')))

print(f'Você digitou os números {numeros}.')
print('O número 9 apareceu {} vez(es).'.format(numeros.count(9)))
if numeros.count(3) == 1:
    print('O número 3 apareceu na {}ª posição.'.format(numeros.index(3)+1))
if numeros.count(3) > 1:
    print('O número 3 apareceu primeiro na {}ª posição.'.format(numeros.index(3) + 1))
if numeros.count(3) < 1:
    print('O número 3 não apareceu')

print('Os valores pares digitados foram: ', end='')

h = 0

for c in numeros:
    if c % 2 == 0:
        h = h + 1
    if h >= 1:
        print(f'{c} ', end='')

if h < 1:
    print('[VOCÊ NÃO DIGITOU NENHUM VALOR PAR].')
