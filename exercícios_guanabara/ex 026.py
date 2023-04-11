f = str(input('Insira uma frase qualquer: ')).lower().strip()
print("""A letra "a" aparece {} vezes.
Além disso, a primeira letra "a" aparece no caractere {}.
E, por fim, a última letra "a" aparece no caractere {}. """.format(f.strip().count('a'), f.find('a')+1, f.rfind('a')+1))
