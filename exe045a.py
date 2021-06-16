print('-*'*25)
print('              \033[07;34;40m       JOKENPÔ      \033[m')
print('-*'*25)

import emoji
from random import randint

computador = randint(0,2)

print('escolha 0 para papel  \U0001f590\uFE0F ')
print('escolha 1 para pedra \u270A')
print('escolha 2 para tesoura \U0001f596')

escolha = int(input(":"))

print('-*'*25)

if (escolha == 0 and computador == 1):
    print(' Parabens!! Você ganhou \U0001f3c6')
elif (escolha == 1 and computador == 2):
    print(' Parabens!! Você ganhou \U0001f3c6')
elif (escolha == 2 and computador == 0):
    print(' Parabens!! Você ganhou \U0001f3c6')
elif escolha == computador:
    print(' O jogo empatou \U0001f91c \U0001f91b  ')
else:
    print(' Você perdeu!! \U0001f61e')

print('-*'*25)



