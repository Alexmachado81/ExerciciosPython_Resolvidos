
soma = 0
for c in range(0,6):
    n = int(input('\033[0;30;42m Informe um numero inteiro: \033[m \n '))
    if n%2 ==0:
        soma = soma + n
print('\033[0;30;41m  A somatoria dos numeros digitados é {} \033[m '.format(soma))