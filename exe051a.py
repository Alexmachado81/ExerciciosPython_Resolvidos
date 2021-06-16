primeiro = int(input('Informe o primeiro termo : '))
razao = int(input('Informe a razão: '))

decimo = primeiro + (10-1)*razao

for c in range(primeiro,decimo,razao):
    print('{}'.format(c), end= "-")
print('FIM')