lista = (int(input('Informe o primeiro numero:')),int(input('Informe o segundo numero:'))
,int(input('Informe o terceiro numero:')),int(input('Informe o ultimo numero:')))
n=0
print('-*'*20)
print( f'Os numeros escolhidos foram {lista}')
if 9 in lista:
    print(f'O numero 9 apareceu {lista.count(9)} vezes ')
else:
    print(f'O numero 9 não foi digitado nenhuma vez')
if 3 in lista:
    print(f'O numero 3 apareceu na posição {lista.index(3)+1}  ')
else:
    print(f'O numero 3 não foi digitado nenhuma vez')
print(f'Os numeros inpares foram:',end='')
for n in lista:
    n %2 == 0
    print(f'{n}',end=" ")

print('\n','-*'*20)
