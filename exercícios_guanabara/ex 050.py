soma = 0

for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if (n + 2) % 2 == 0:
        soma = soma+n

print(soma)
