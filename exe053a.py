print('\033[0;33;40m*-\033[m'*20)
print('         Analisador de frase   ')
print ('      ------PALINDROMO-------')
print('\033[0;33;40m*-\033[m'*20)

frase = str(input('         Digite uma frase \n')).strip().upper()

separar = frase.split()
junto = ''.join(separar)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print(" A frase \033[1;32m {} \033[m \n lida de trás para frente:\033[1;32m {}\033[m, \n é um PALINDROMO".format(junto,inverso))
else:
    print(" A frase \033[1;32m {} \033[m \n lida de trás para frente:\033[1;32m {}\033[m, \n \033[1;31m NÃO \033[m é um PALINDROMO".format(junto, inverso))

