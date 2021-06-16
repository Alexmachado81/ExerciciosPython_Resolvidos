numero = int(input('Digite um numero de 0 a 9999: \n'))

unid = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print(' Analisando o numero {} '.format(numero))
print(' Unidade : {}'.format(unid))
print(' Dezena : {}'.format(dez))
print(' Centena : {}'.format(cen))
print(' Milhar : {}'.format(mil))


