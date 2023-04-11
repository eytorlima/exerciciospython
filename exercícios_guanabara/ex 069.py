cp = 0
cm = 0
ch = 0
cmi = 0

while True:
    print('================')
    print('CADASTRE UMA PESSOA')
    y = int(input('Idade: '))
    g = str(input('Sexo[M/F]: ')).strip().title()[0]
    while g not in 'MF':
        if g != 'm' or 'f':
            g = str(input('Sexo[M/F]: ')).strip().title()[0]
    if g == 'm' or 'f':
        print('================')
    cp = cp + 1

    if y < 20 and g == 'F':
        cm = cm + 1

    if y > 18:
        cmi = cmi + 1

    if g == 'M':
        ch = ch + 1

    p1 = str(input('Quer continuar cadastrando pessoas?[S/N]: ')).strip().title()[0]
    while p1 not in 'SN':
        if p1 != 's' or 'n':
            p1 = str(input('Quer continuar cadastrando pessoas?[S/N]: ')).strip().title()[0]
    if p1 == 'N':
        break

print('CADASTROS FINALIZADOS')
print(f'Foram {cp} pessoa(s) cadastradas. Dentre elas:\n'
      f'{cmi} pessoa(s) possuem mais de 18 anos.\n'
      f'{ch} é(são) homem(ns).\n'
      f'{cm} é(são) mulher(es) com menos de 20 anos.')
