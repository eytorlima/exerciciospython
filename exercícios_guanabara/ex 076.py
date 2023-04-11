produtos = ('pao', 10,
            'agua', 5,
            'soja', 40,
            'brinquedo', 14,
            'cebola', 8,
            'cachorro', 7,
            'gato', 5)

print('='*40)
print('{:^25}'.format('PREÇOS'))
print('='*40)
# print('')
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f' R$ {produtos[c]:>5.2f}')
print('='*40)