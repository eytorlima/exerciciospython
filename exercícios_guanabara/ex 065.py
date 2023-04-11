p1 = 'S'

while p1 == 'S':
    n = 0
    c = 0
    m = 0
    maior = 0
    menor = 0
    mm = 1
    while n != 999:
        n = int(input('Digite números inteiros [FLAG = 999]: '))
        c = c+1
        m = m+n

        if n != 999:
            if n > maior and n != 999:
                maior = n

            if mm == 1:
                menor = maior

            if n < menor and n != 999:
                menor = n

        mm = mm - 1

    c = c-1

    if c == 0:
        print('FIM')

    if c > 0:
        m = (m - 999) / c
        print('Você digitou {} números.\nA média entre eles é {}.'.format(c, m))
        print('O maior número foi {}.\nO menor número foi {}.'.format(maior, menor))

    p1 = str(input('Deseja continuar digitando valores?[S/N]: ')).strip().title()[0]

if p1 == 'N':
    print('Programa encerrado.')
