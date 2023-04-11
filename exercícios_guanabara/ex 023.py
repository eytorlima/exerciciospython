n = str(input('Insira um número inteiro com até 4 digitos: '))
m = (n[:4].split())
if len(n) >= 5:
    print("""Seu número possui mais digitos do que o esperado, portanto, serão considerados apenas
     os 4 primeiros caracteres da esquerda para a direita.""")
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""". format(m[0][3], m[0][2], m[0][1], m[0][0]))
