numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número de 0 a 20: '))
c = 0
while 0 > n or n > 20:
    n = int(input('Tente novamente. Digite um número de 0 a 20: '))

if 0 <= n <= 20:
    print('Você digitou o número {}.'.format(numeros[n]))
