import random
print('Vamos jogar Joken Pô!')
uc = str(input('Pedra, Papel ou Tesoura?: ')).strip().lower().capitalize()

p = str('Pedra')
pa = str('Papel')
t = str('Tesoura')
cclist = [p, pa, t]
cc = random.choice(cclist)

print('Você escolheu {}\nEu escolhi {}!\nAnalisando...'.format(uc, cc))

if uc == cc:
    print('Ops! Deu empate!')

if uc == p and cc == pa:
    print('Eu ganhei!!!')

if uc == p and cc == t:
    print('Você ganhou!!!')

if uc == pa and cc == p:
    print('Você ganhou!!!')

if uc == pa and cc == t:
    print('Eu ganhei!!!')

if uc == t and cc == pa:
    print('Você ganhou!!!')

if uc == t and cc == p:
    print('Eu ganhei!!!')

elif uc != t and uc != p and uc != pa:
    print('Escolha uma das três opções!')
