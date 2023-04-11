import random
print('===== PAR OU IMPAR =====')

n = 0

print('Vamos jogar par ou impar!')

while True:
    cpu = random.randint(0, 10)
    user = int(input('Diga um número de 0 a 10: '))
    upi = str(input('Você escolhe par ou impar?[P/I]: ')).strip().title()[0]

    print(f'Você jogou {user} e o computador jogou {cpu}.')

    if upi == 'P' and (cpu+user) % 2 != 0:
        print('DEU IMPAR!')
        print('GAME OVER!')
        print(f'Você venceu {n} vezes.')
        break

    if upi == 'I' and (cpu+user) % 2 == 0:
        print('DEU PAR!')
        print('GAME OVER!')
        print(f'Você venceu {n} vezes.')
        break

    if upi == 'P' and (cpu + user) % 2 == 0:
        print('DEU PAR!')
        print('Você venceu, continue jogando!')

    if upi == 'I' and (cpu + user) % 2 != 0:
        print('DEU IMPAR!')
        print('Você venceu, continue jogando!')

    print('')

    n = n+1
