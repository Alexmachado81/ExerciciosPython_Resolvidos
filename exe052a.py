numero = int(input('Informe um numero: '))
soma =0
for c in range(1,numero+1):
    if numero % c == 0:
        soma = soma +1
if soma == 2:
    print(' Este numero informado {} é primo'.format(numero))
else:
    print(' Este numero informado {}, não é primo'.format(numero))