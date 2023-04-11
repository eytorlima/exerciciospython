n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = float(((n1+n2)/2))

if m < 5:
    print('Aluno reprovado.')

elif 5 < m <= 6.9:
    print('Aluno em recuperação.')

else:
    print('Aluno aprovado.')
