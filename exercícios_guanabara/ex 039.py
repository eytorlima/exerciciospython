y = int(input('Qual a sua idade?: '))

if y < 18:
    print('Fique atento para a data de alistamento, restam {} ano(s) para que você possa se alistar!'.format(18-y))

elif y==18:
    print('Fique atento, você já pode realizar seu alistamento!')

else:
    print('Fique despreocupado! Sua data de alistamento já venceu há {} ano(s).'.format(y-18))
