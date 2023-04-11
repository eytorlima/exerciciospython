s = c = 0

while True:
    n = int(input('Digite um número [FLAG = 999]: '))
    if n == 999:
        break
    c = c+1
    s = s+n

print(f'Você digitou {c} números.\nA soma entre eles é igual a {s}')
