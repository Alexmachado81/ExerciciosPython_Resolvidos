cont = 0
while True:
    numero  = int(input('Informe o numero que você quer ver a tabuada[digite um numero negatigo para parar]:'))
    if numero < 0:
        break
    print('-'*20)
    while cont <= 10:
        mult = cont * numero
        print(f'{cont} x {numero} = {mult}')
        cont +=1
    print('-' * 20)
    cont = 0
print('-' * 20)
print('Programa finalizado')
print('-' * 20)
