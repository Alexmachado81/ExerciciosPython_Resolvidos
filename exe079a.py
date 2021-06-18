numeros = []

while True:
    x = int(input('Digite um valor:'))
    if x not in numeros:
        numeros.append(x)
    else:
        print(f'O Numero digitado {x} já esta na lista e não será incluido!')
    stop = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('Opção invalida, Deseja continuar? [S/N]')).upper().strip()[0]
    if stop == 'N':
        break
print('-'*40)
numeros.sort()
print(f'Os Valores digitados foram {numeros}')
print('-'*40)