s = 0
cc = 0
for c in range(1, 501):
    if (c+1) % 2 == 0 and c % 3 == 0:
        cc = cc+1
        s = s + c

print('São {} valores solicitados, a soma entre eles é {}.'.format(cc, s))
