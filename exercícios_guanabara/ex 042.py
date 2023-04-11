t1 = float(input('Valor 1: '))
t2 = float(input('Valor 2: '))
t3 = float(input('Valor 3: '))

if (t1+t2)>t3 and (t1+t3)>t2 and (t2+t3)>t1:
    print('Essas 3 retas podem formar um triângulo.')

    if t1 != t2 != t3:
        print('Este é um triângulo escaleno.')

    if t1 == t3 and t3 != t2 or t1 == t2 and t2 != t3 or t2 == t3 and t2 != t1:
        print('Este é um triângulo isósceles.')

    if t1 == t2 and t2 == t3:
        print('Este é um triângulo equilátero.')

else:
    print('Essas 3 retas não podem formar um triângulo.')
