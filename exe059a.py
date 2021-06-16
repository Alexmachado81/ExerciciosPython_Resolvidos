num1 = int(input(" Informe un numero qualquer:"))
num2 = int(input(" Informe outro numero qualquer:"))
escolha = 0

while escolha != 5:
    print('-'*20)
    print(' [1] soma\n',
          '[2] multiplicação\n',
          '[3] maior\n',
          '[4] novos numeros\n',
          '[5] sair\n')
    print('-'*20)
    escolha = int(input('Informe qual sua escolha:'))
    if escolha ==1:
        resultado = num1 + num2
        print(' A soma dos valores escolhidos é : {}'.format(resultado))
    elif escolha ==2:
        resultado = num1 * num2
        print(' A multiplicação dos valores escolhidos são: {}'.format(resultado))
    elif escolha ==3:
        if num1 > num2:
            print('O maior numero é {}'.format(num1))
        else:
            print(' O maior numero escolhido é {}'.format(num2))
    elif escolha == 4:
        num1 = int(input(" Informe un numero qualquer:"))
        num2 = int(input(" Informe outro numero qualquer:"))
print('Fim do programa')



