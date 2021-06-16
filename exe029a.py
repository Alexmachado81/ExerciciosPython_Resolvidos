vel = int(input('Informe qual a velocidade que voce esta dirigendo:\n'))

if vel >= 80:
    multa=(vel-79)*7
    print(' Você está acima da velocidade permitida e foi multado em {:.2f} reais'.format(multa))
else:
    print(' Parabens! Você está andando dentro da velocidade permitida')