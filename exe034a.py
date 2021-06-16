sal = float(input(" Informe o seu salário: \n"))

if sal <= 1250:
    nsal = sal*1.15
    print(' Parabens! Você recebeu um aumento de 15% e passará a ganhar R${:.2f}'.format(nsal))
else:
    nsal = sal*1.1
    print(' Parabens! Você recebeu um aumento de 10% e passará a ganhar R${:.2f}'.format(nsal))