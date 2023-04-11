y = int(input('Qual a sua idade?: '))

if y <= 9:
    print('Categoria {}MIRIM {}.'.format('\033[1;34;107m ', '\033[m'))

elif 9 < y <= 14:
    print('Categoria {}INFANTIL {}.'.format('\033[1;31;107m ', '\033[m'))

elif 14 < y <= 19:
    print('Categoria {}JUNIOR {}.'.format('\033[1;32;107m ', '\033[m'))

elif y == 20:
    print('Categoria {}SÊNIOR {}.'.format('\033[1;33;107m ', '\033[m'))

else:
    print('Categoria {}MASTER {}.'.format('\033[1;30;107m ', '\033[m'))
