import random

nome1 = str(input('Informe o primeiro nome :\n'))
nome2 = str(input('Informe o segundo nome :\n'))
nome3 = str(input('Informe o terceiro nome :\n'))
nome4 = str(input('Informe o quarto nome :\n'))

lista = [nome1,nome2,nome3,nome4]

escolhido = random.shuffle(lista)

print(' A ordem de apresentação será :')
print(lista)