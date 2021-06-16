a = int(input('Informe o primeiro numeros inteiros: \n'))
b = int(input('Informe o segundo numeros inteiros: \n'))
c = int(input('Informe o terceiro numeros inteiros: \n'))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

medio = a
if b>menor and b<maior:
    medio = b
if c>menor and c<maior:
    medio = c


print(' O menor numero digitado foi {}'.format(menor))
print(' O maior numero digitado foi {}'.format(maior))
print(' O numero entre o maior e o menor numero é {}'.format(medio))
