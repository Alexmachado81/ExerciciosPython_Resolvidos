lista = ('APRENDER','PROGRAMAR','LIMGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR')

print("-"*40)
print(f'{"Analise de vogais":^40}')
print("-"*40)
for c in lista:
    print(f'\nNa palavra "', f'{c:^10}', f'" temos:',end=" ")
    for letra in c:
        if letra.lower() in 'aeiou':
            print (f'{letra}',end=" ")
print('\n\n',"-"*40)