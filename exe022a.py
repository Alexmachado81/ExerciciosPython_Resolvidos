nome = str(input(' Digite seu nome completo:\n')).strip()
separa = nome.split()

print(' Analisando seu nome ... ')
print(' Seu nome completo em maiúsculas é {}'.format(nome.upper()))
print(' Seu nome completo em minústulas é {}'.format(nome.lower()))
print(' Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print(' Seu primeior nome é {} e possui {} letras'.format(separa[0], len(separa[0])))










