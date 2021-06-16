cont = -1
num = 0
num2 = 0

while num != 999:
    num = int(input('Informe um numero inteiro ou [digite 999 para parar]:'))
    cont+=1
    #print('{} +'.format(num),end=' ')
    if num != 999:
        soma = num + num2
        num2 = soma
print('A soma dos {} numeros digitados é {}'.format(cont,soma))