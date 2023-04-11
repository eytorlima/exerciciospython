import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

print("""O dado 1 gerou o número \033[1;31;107m {} \033[m.
O dado 2 gerou o número \033[1;34;107m {} \033[m.
A soma dos dados é \033[1;30;107m {} \033[m.""".format(d1, d2, (d1+d2)))
