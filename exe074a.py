from random import randint

lista = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os numeros sortiados foram:', end=" ")
for c in lista:
    print(f'{c}',end=" ")
print(f'\nO maior numero sorteado foi {max(lista)}')
print(f'O menor numero sorteado foi {min(lista)}')

