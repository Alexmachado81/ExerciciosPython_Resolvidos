from datetime import date

print(' Analise de categoria ')

ano = int(input(' Informe o ano em que você nasceu: \n'))

idade = (date.today().year)-ano

if idade <= 9:
    print( 'Sua categoria é MIRIN')
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade > 19 and idade <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')