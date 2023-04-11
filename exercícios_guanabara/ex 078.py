valores = []
maior = menor = p = 0

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    if v != 0:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]

print(f'A lista criada foi: {valores}')
print(f'O maior valor foi: {maior} na(s) posição(ões) ', end='')
for i, n in enumerate(valores):
    if n == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi: {menor} na(s) posição(ões) ', end='')
for i, n in enumerate(valores):
    if n == menor:
        print(f'{i}... ', end='')
