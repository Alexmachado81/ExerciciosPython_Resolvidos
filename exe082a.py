lista = []
impar = []
par = []
while True:
    num = int(input('Informe um numero inteiro:'))
    lista.append(num)
    if num%2 ==0:
        par.append(num)
    else:
        impar.append(num)
    stop = str(input('Deseja continuar inserindo numeros em sua lista?[S/N]')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('Opção invalida, Digite novamente[S/N]')).upper().strip()[0]
    if stop in 'N':
        break
print(f'Os numeros da sua lista são {lista}')
print(f'Os numeros pares digitador foram {par}')
print(f'Os numeros impares digitador foram {impar}')