numeros = []

for c in range(0,5):
    n = int(input('Informe um numero inteiro:'))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Numero inserido da ultima posição')
    else:
        pos=0
        while pos < len(numeros):
            if n<= numeros[pos]:
                numeros.insert(pos,n)
                print(f'Numero inserido na {pos} posição')
                break
            pos +=1

print('-*'*40)
print(numeros)
