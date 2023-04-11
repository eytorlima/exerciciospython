v = str(input('Insira o sexo do usuário (M/F): ')).strip().title()[0]

while v not in 'MF':
    if v != 'M' or 'F':
        v = str(input('Insira um valor válido: ')).strip().title()[0]
if v == 'm' or 'f':
    print('Ok. Sexo {} computado.'.format(v))
