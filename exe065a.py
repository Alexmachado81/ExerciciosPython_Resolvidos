cond = 'S'
num = quant = soma = maior = menor =0

while cond in 'Ss':
    num = int(input(' Informe um numero:'))
    quant += 1
    soma += num
    cond = str(input('Quer Continuar?[S/N]')).upper().strip()[0]
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma/quant
print('Você digitou {} numero(s) \n'
      'A soma do(s) numero(s) é {} \n'
      'Sua media é {:.1f} \n'
      'O maior numero digitado foi {} \n'
      'O menor numero digitado foi {}'.format(quant,soma,media,maior,menor))
