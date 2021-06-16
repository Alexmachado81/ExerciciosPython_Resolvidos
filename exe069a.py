homem = menor = maior = conte =0
print('-'*30)
print('CADASTRO DE DADOS')
print('-'*30)

while True:
    idade = int(input('Informe sua idade :'))
    conte +=1
    sexo = str(input('Informe seu sexo [M/F] :')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Opção invalida. Informe seu sexo [M/F] :')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem +=1
    if idade < 20 and sexo =='F':
        menor += 1
    print('-'*30)
    STOP = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while STOP not in 'SN':
        STOP = str(input('Opção invalida. Deseja continuar? [S/N]')).strip().upper()[0]
    if STOP =='N':
        break
    print('-' * 30)

print('-'*30)
print(' DADOS COLETADOS ')
print('-'*30)
print(f'foram cadastradas {conte} pessoas,\n {maior} pessoas maiores de idade,\n {homem} pessoas do sexo masculino\n e {menor} mulheres menores de 20 anos.')
