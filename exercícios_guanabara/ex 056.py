import time

si = 0
cf = 0
nh = 0
mih = 0

for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa?: '.format(c))).strip().title()
    idade = int(input('Qual a idade da {}ª pessoa?: '.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa? (Feminino ou Masculino): '.format(c))).strip().title()
    print('')
    time.sleep(0.25)

    if idade != 0:
        si = si + idade

    if sexo == str('Masculino') and idade > mih:
        nh = nome
        mih = idade

    if sexo == str('Feminino') and idade < 20:
        cf = cf+1

print("""A média de idade é {}.
O homem mais velho se chama {} e tem {} anos.
Existem {} mulhere(s) com menos de 20 anos.""".format((si/4), nh, mih, cf))
