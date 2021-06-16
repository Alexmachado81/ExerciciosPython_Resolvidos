num = int(input(' Informe um numero inteiro: \n'))
resultado = num % 2
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))