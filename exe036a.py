print('*'*20)
print(' Analise de emprestimo ')
print('*'*20)

vcasa = int(input('Informe o valor do imóvel :\n'))
vsal = int(input('Informe o seu salario: \n'))
tempo = int(input('Informe em quantos anos você pretente efetuar o financiamento : \n'))

if vcasa <= (vsal*.3*(tempo*12)):
    print(' Seu financiamento de R${:.2f}, esta aprovado para o pagamento dentro do perido de {} anos.'.format(vcasa,tempo))
elif vcasa > (vsal*.3*(tempo*12)):
    print(' Seu financiamento foi \033[7;31;40m Negado \033[m')
    ref=str(input(' Quer tentar um periodo maior para pagamento? sim ou não')).lower()
    elif ref == 'sim':
        tempo1 = int(input('informe o novo periodo para financiamento: \n'))
    elif vcasa <= (vsal*.3*(tempo1*12)):
        print(' Seu financiamento de R${:.2f}, esta aprovado para o pagamento dentro do perido de {} anos.'.format(vcasa,tempo1))
else:
    print(' Seu financiamento foi \033[7;31;40m Negado \033[m')