import random

maior = menor = 0

n1 = random.randint(1, 10)
if n1 > 0:
    maior = n1
    menor = n1

n2 = random.randint(1, 10)
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3 = random.randint(1, 10)
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

n4 = random.randint(1, 10)
if n4 > maior:
    maior = n4
if n4 < menor:
    menor = n4

n5 = random.randint(1, 10)
if n5 > maior:
    maior = n5
if n5 < menor:
    menor = n5

lista = (n1, n2, n3, n4, n5)

print('Os valores sorteados foram: {}'.format(lista))
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
