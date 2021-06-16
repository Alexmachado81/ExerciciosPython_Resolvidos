print('*'*25)
print(' Calculadora de IMC ')
print('*'*25)

altura = int(input('Informe sua altura em centimetros : \n'))
peso = int(input('Informe seu peso em quilogramas : \n'))

alt = altura/100
IMC = peso / (alt**2)

if IMC < 18.5:
    print('Você está abaixo do peso ')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no peso Ideal')
elif IMC >= 25 and IMC < 30:
    print('Você está com Sobrepeso')
elif IMC >= 30 and IMC < 40:
    print('Você está com Obesidade')
elif IMC >= 40:
    print('Você está com Obesidade Mórbida')
