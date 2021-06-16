from datetime import date
ano = date.today().year
usuario = 1
maior = 0
menor = 0

for c in range(1,8):
    idade = int(input(' Informe o ano em que voce nasceu usuario {}: '.format(usuario)))
    usuario += 1
    if 21 <= (ano-idade):
        maior += 1
        #print( " usuario {}, você nasceu em {} e portanto é \033[0;32m maior \033[m de idade".format(usuario,idade))
    else:
        menor += 1
        #print(" usuario {}, você nasceu em {} e portanto é \033[0;31m menor \033[m de idade".format(usuario, idade))

print(' No total deste grupo, temos {} pessoas maiores de idade'.format(maior))
print(' e temos {} pessoas menores de idade.'.format(menor))



