num1 = int(input('Informe um numero inteiro \n'))
num2 = int(input('Informe outro numero inteiro \n'))

if num1 > num2:
    print(' O primeiro numero {} é maior que o segundo numero {}'.format(num1,num2))
elif num2 > num1:
    print(' O segundo numero {} é maior que o primeiro numero {}'.format(num2,num1))
else:
    print('Os numeros {} e {} são iguais'.format(num1,num2))