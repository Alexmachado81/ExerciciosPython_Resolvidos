print('*'*30)
print('    Condições de pagamento')
print('*'*30)

valor = int(input('Informe o valor do produdo em reais : \n'))

print('*\n'*80)
print('Para o produto informado temos 4 condições de pagamento:\n',
      'Condição 1 = Pagamento em dinheiro\n',
      'Condição 2 = Pagamento avista no cartão \n',
      'Condição 3 = Pagamento em ate 2x no cartão \n',
      'Condição 4 = Pagameento em 3x ou mais vezes no cartão\n')
print('*'*80)

val1 = valor-valor*.1
val2 = valor-valor*.05
val3 = valor+valor*.2

pg = int(input(' Qual a forma que você pretende fazer o pagamento? Opção 1,2,3 ou 4 ?\n'))

if pg == 1:
    print( ' Para esta opção você recebeu um desconto de 10% e ira pagar R${}'.format(val1))
elif pg == 2:
    print(' Para esta opção você recebeu um desconto de 5% e ira pagar R${}'.format(val2))
elif pg == 3:
    print(' O valor a ser pago será R${}'.format(valor))
elif pg == 4:
    print(' O valor a ser pago será R${}'.format(val3))
else:
    print('Opção de pagamento invalida')
