lista = []
cont = 0
while True:
    num = int(input('Informe um numero inteiro:'))
    lista.append(num)
    if num == 5:
        cont +=1
    stop = str(input('Deseja continuar inserindo numeros em sua lista?[S/N]')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('Opção invalida, Digite novamente[S/N]')).upper().strip()[0]
    if stop in 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f'Em sua lista o numero cinco foi digitado {cont}')