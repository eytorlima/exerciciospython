import random
import time
print('GERADOR DE NÚMEROS\n')

n = random.randint(1, 100)
chute = 0
c = 10

print('Gerei um número de 1 a 100, tente acertar qual foi: ')
time.sleep(0.35)

while chute != n and c > 0:
    chute = int(input('\nVocê tem {} chance(s)!: '.format(c)))
    time.sleep(0.15)
    c = c-1

    if c > 0:
        if chute != n:
            if chute < n:
                print('Errou! Chute um valor mais alto!')
            if chute > n:
                print('Errou! Chute um valor mais baixo!')
        time.sleep(0.35)
        if chute == n:
            print('Parabéns, você acertou!')
            time.sleep(0.35)

    if c == 0:
        print('Infelizmente suas chances acabaram.')
