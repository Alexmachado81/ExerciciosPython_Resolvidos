from random import randint
numero = randint(0,5)
print('+-'*30)
print( ' estou pensando em um numero entre 0 e 5 tente adivinhar...')
print('+-'*30)
jogador = int(input(' Em que numero eu pensei?\n'))

if numero == jogador:
    print('Parabens voce venceu!')
else:
    print('Voce perdeu! quer tentar novamente a sorte?')
