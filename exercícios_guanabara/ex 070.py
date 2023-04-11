print('----- LEITOR DE COMPRAS -----')

maior = menor = t = mm = vpb = npb = 0
cmm = 1

while True:
    np = str(input('Insira o nome do produto: ')).strip()
    v = float(input('Insira o valor do produto: R$'))

    t = t + v

    if v > 1000:
        mm = mm+1

    if v > maior:
        maior = v

    while cmm == 1:
        menor = v
        vpb = v
        npb = np

        cmm = cmm - 1

    if v < menor:
        vpb = v
        npb = np

    p = str(input('Quer continuar registrando produtos?[S/N]: ')).strip().title()[0]
    while p not in 'SN':
        if p != 'S' or 'N':
            p = str(input('Quer continuar registrando produtos?[S/N]: ')).strip().title()[0]
    if p == 'N':
        print('==========')
        break

    if p == 'S':
        print('==========')

print('\nPRODUTOS REGISTRADOS COM SUCESSO.')
print(f'O total gasto foi de R${t}')
print(f'Há {mm} produtos custando mais de R$1000,00')
print(f'O produto mais barato registrado foi {npb} e custou {vpb}')
