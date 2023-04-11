times = ('Atlético-MG', 'Botafogo', 'Corinthians', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional',
         'Palmeiras', 'Santos', 'São Paulo', 'Vasco', 'Juventude', 'Avaí', 'Terezina FC', 'Natal FC', 'Barcelona',
         'Real Madrid', 'Figueiredo FC', 'Paulistinha FC')

print('{}'.format('='*20))
print('Os cinco primeiro colocados são {}.'.format(times[0:5]))
print('{}'.format('='*20))
print('Os últimos quatro últimos colocados são {}.'.format(times[-4:20]))
print('{}'.format('='*20))
print('Os times em ordem alfabética são {}'.format(sorted(times)))
print('{}'.format('='*20))
print('Corinthians está na {}ª posição'.format(times.index('Corinthians')+1))
