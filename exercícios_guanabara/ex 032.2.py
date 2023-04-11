ano = int(input('Insira um ano: '))
if ano > 0:
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            print(f'O ano {ano} não é bissexto')
        else:
            print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
