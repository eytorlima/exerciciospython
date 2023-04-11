h = float(input('Qual é a sua altura em metros?: '))
w = float(input('Qual é o seu peso em quilos?: '))
imc = float(w/(h*h))

print('Seu IMC é de {:.3f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal.')

elif 18.5 < imc < 25:
    print('Você está no peso ideal!')

elif 25 < imc < 30:
    print('Você está um pouco acima do peso ideal.')

elif 30 < imc < 40:
    print('O seu IMC o classifica com Obesidade.')

else:
    print('O seu IMC o classifica com Obesidade Mórbida.')
