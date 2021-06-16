sid = 0
velho = 0
novo = 0
for c in range(1,5):
    print('\033[0;30;41m ---- {}ª PESSOA ----\033[m'.format(c))
    nome = str(input('Infome o seu nome:'))
    idade = int(input('Informe sua idade:'))
    sexo = str(input('Informe seu sexo (M/F):')).strip()
    print('')
    sid = sid + idade
    if c == 1:
        velho = idade
        vnome = nome
    if idade < 20:
        novo +=1
    else:
        if velho < idade:
            velho = idade
            vnome = nome
grupo = c-novo
media = sid/4
print('-'*76)
print('A media das idades é {}'.format(media))
print('No grupo temos {} pessoas com mais de 20anos e {} pessoas abaixo de 20anos'.format(grupo,novo))
print ('A pessoal mais velha do grupo é {} e possui {}anos'.format(vnome,velho))
print('-'*76)

