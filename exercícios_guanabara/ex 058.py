import random
n = random.randint(0, 10)
chutes = 0
c = int(input('Pensei em um número de 0 a 10.\nTente adivinhar o número: '))
while c != n:
    chutes = chutes + 1
    c = int(input('Tente novamente: '))

print('Parabéns, você acertou em {} tentativa(s)!'.format(chutes))
