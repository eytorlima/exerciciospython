cn = 0
for c in range(0, 7):
    n = int(input('Em que ano você nasceu?: '))
    m = 2022 - n
    if m >= 21:
        cn = cn+1
print('{} pessoas dessa lista já atingiram a maior de idade.'.format(cn))
