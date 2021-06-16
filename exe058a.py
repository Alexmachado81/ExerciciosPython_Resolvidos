from random import randint
num = randint(1,10)
conta = 1
print('-'*30)
print('--- Jogo de adivinhação ---')
print('-'*30)
print('\033[0;31;40m Qual o numero que eu estou pensando? \033[m')


acertou = False

while not acertou:
    jogador = int(input(' Informe um numero de 1 a 10 :'))
    conta += 1
    if jogador == num:
        acertou = True
    else:
        if jogador > num:
            print(" Alto demais.. tente novamente ")
        elif jogador < num:
                print(" Baixo demais .. tente novamente ")
print(' Parabens! Voce acertou.\n Foram necessarios {} tentativas para acertar o numero'.format(conta))


