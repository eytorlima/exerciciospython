import random
i = random.randint(0, 5)
r = int(input('Pensei em um número de 0 a 5, tente adivinhar qual é: '))
if r == i:
    print('Parabéns, você acertou!')
else:
    print('Poxa, não foi dessa vez! Eu pensei no número {i}')
