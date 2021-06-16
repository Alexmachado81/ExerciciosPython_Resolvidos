listagem = ('Caneta',4.05,
            'Regua',3.00,
            'Caderno', 12.50,
            'Lapis',3.75,
            'Apontador',9.00,
            'Caixa de Clips', 13.80,
            'Grampeador',29.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<30}',end=" ")
    else:
        print(f'R$ {listagem[pos]:>6.2f}')
print('-'*40)
