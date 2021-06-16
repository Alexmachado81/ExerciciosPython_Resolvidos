barato = preço = cont = total = 0

while True:
    prod = str(input('Informe o nome do produto: '))
    preço = int(input("Informe o valor do produto: "))
    total = total + preço
    if barato > preço or barato == 0:
        barato = preço
        nome = prod
    if preço > 1000:
        cont +=1
    stop = str(input(' Deseja continuar? [S/N]')).upper().strip()[0]
    while stop not in 'SN':
        stop = str(input('Opção invalida. Deseja continuar? [S/N]')).strip().upper()[0]
    if stop =='N':
        break
print('-'*30)
print(f" Você gastou um total de R${total},"
      f" O item mais barato que voce comprou foi {nome} e custou R$ {barato:.2f}"
      f" Você comprou {cont} itens acima de R$1.000,00")
print('-'*30)
print(' Obrigado pela preferencia e Volte sempre')