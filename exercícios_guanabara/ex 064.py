n = 0
c = -1
s = 0

while n != 999:
    n = int(input('Digite números inteiros [FLAG = 999]: '))
    c = c+1
    s = s+n

s = s-999

print('Você digitou {} números.\nA soma entre eles é {}.'.format(c, s))
