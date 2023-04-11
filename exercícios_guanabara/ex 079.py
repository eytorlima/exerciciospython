lista = []
while True:
    n = int(input('Insira um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado.')
    else:
        print('Ops! Esse valor já foi adicionado anteriormente.')
    p = str(input('Quer continuar?[S/N]: ')).strip().title()[0]
    if p not in 'SN':
        p = str(input('Quer continuar?[S/N]: ')).strip().title()[0]
    if p == 'N':
        print('Ok. Número(s) coletado(s).')
        break
print(lista)
