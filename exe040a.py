print('-'*25)
print('Analise academica')
print('-'*25)
nota1 = float(input('Informe a sua primeira nota : \n'))
nota2 = float(input('Informe a sua segunda nota : \n'))

media = (nota1 + nota2)/2

if media < 5:
    print(' Infelizmente você esta reprovado, estude mais que você consegue')
elif media >= 5 and media < 6.9:
    print('Ainda há tempo, vamos estudar, pois você esta em recuperação')
else:
    print('Parabens! Você está aprovado')
