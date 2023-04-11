print('{}\n{:^20}\n{}'.format('='*20, 'BANCO', '='*20))

n = int(input('Qual valor você deseja sacar?: R$'))

ncinq = nvinte = ndez = num = 0

while True:
    while n >= 50:
        n = n - 50
        ncinq = ncinq + 1

    if ncinq >= 1:
        print(f'{ncinq} nota(s) de cinquenta.')

    while n >= 20:
        n = n - 20
        nvinte = nvinte + 1

    if nvinte >= 1:
        print(f'{nvinte} nota(s) de vinte.')

    while n >= 10:
        n = n - 10
        ndez = ndez + 1

    if ndez >= 1:
        print(f'{ndez} nota(s) de dez.')

    while 0 < n < 10:
        n = n - 1
        num = num + 1

    if num >= 1:
        print(f'{num} nota(s) de um.')

    if n == 0:
        break

print('''TOTAL SACADO: R${},00'''.format(((ncinq*50)+(nvinte*20)+(ndez*10)+(num*1))))
