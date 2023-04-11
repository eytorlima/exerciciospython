palavras = ('APRENDER', 'PROGRAMAR', 'CALCULADORA', 'TABLET', 'CELULAR', 'TECLADO', 'GRATIS', 'ESTUDAR',
            'CAIXAO', 'ESCOLA', 'CELULAR', 'BORRACHA', 'LAPIS', 'CADERNO', 'APAGADOR')

print('-'*20)
print('{:^20}'.format('VOGAIS'))
print('-'*20)

for p in range(0, len(palavras)):
    print(f'Na palavra {palavras[p]}, temos:', end='')
    if 'A' in palavras[p]:
        print(' a', end='')

    if 'E' in palavras[p]:
        print(' e', end='')

    if 'I' in palavras[p]:
        print(' i', end='')

    if 'O' in palavras[p]:
        print(' o', end='')

    if 'U' in palavras[p]:
        print(' u', end='')
    print('')
