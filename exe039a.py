from datetime import date

ano = int(input('Informe o ano em que você nasceu: \n'))

idade = (date.today().year )-ano

tempo = idade - 18
tempo1 = 18 - idade

if idade == 18:
    print('Parabens! Você esta no periodo de alistamento')
elif idade > 18:
    print('Você já passssou do periodo de alistamento a {} anos'.format(tempo))
elif idade < 18:
    print('Você esta quase no periodo de alistamento, falta apenas {} anos'.format(tempo1))

print('*'*20)
print(' Patria ama Brasil')
print('*'*20)