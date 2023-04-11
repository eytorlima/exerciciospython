v = float(input('Insira a velocidade em que você percorreu a via: '))

print('Analisando velocidade...')
if v >= 80:
    print("""Aparentemente você excedeu o limite de velocidade da via.
    Você receberá uma multa no valor de R${:.2f} """.format((v-80)*7))
else:
    print("""Ok, você estava dentro do limite de velocidade, siga em segurança.""")
