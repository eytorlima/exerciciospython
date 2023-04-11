print('PESO IDEAL 2.0')
h = float(input('Insira sua altura: '))
g = str(input('Insira seu sexo [M/F]: ')).strip().title()[0]
while g not in 'MF':
    g = str(input('Insira seu sexo [M/F]: ')).strip().title()[0]
if g == 'M':
    print(f'Seu peso ideal é {(h*72.7)-58:.2f} quilos.')
if g == 'F':
    print(f'Seu peso ideal é {(h*62.1)-44.7:.2f} quilos.')
