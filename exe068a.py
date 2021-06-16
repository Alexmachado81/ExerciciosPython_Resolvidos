from random import randint
cont = 1
computador = randint(0,10)

while True:
    jogador = int(input('Digite um valor inteiro: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input('Faça sua escolha: PAR ou IMPAR ?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total é {total}')
    if tipo == 'P':
        if total%2 == 0:
            print('Você venceu!!')
            cont += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Você venceu!!')
            cont += 1
        else:
            print('Você perdeu!!')
            break
    print('Está com sorte!! Vamos jogar novamente')
print('-*'*30)
print(f' GAME OVER !! \n Voce jogou {cont} vezes até perder !!!')
print('-*'*30)


