maior = 0
menor = 0

for c in range(1, 7):
    peso = float(input('Qual o peso da {}ª pessoa em kg?: '.format(c)))

    if c == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é de {:.2f} quilos e o menor peso é de {:.2f} quilos.'.format(maior, menor))
