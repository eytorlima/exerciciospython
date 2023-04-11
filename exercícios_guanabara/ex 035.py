t1 = float(input('Valor 1: '))
t2 = float(input('Valor 2: '))
t3 = float(input('Valor 3: '))

if (t1+t2)>t3 and (t1+t3)>t2 and (t2+t3)>t1:
    print('Essas 3 retas podem formar um triângulo.')

else:
    print('Essas 3 retas não podem formar um triângulo.')
