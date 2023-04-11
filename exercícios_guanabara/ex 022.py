n = str(input('Insira seu nome completo: '))
u = n.strip().upper()
l = n.strip().lower()
letras = n.split()
ll = ''.join(letras)

print("""Seu nome em letras maiúsculas é {}.
Seu nome em letras minúsculas é {}.
Seu nome possui {} letras.
Seu primeiro nome possui {} letras.""".format(u, l, len(ll), len(letras [0])))
