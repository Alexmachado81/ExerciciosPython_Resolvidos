num = int(input('Informe o primeiro termo:'))
razao = int(input('Informe a razão:'))
con =1
termo = num
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while con<=total:
        termo = termo+razao
        con +=1
        print(" {} -".format(termo),end=" ")
    print("pausa")
    mais = int(input('quantos termos voce quer mostras a mais?'))
print('Progressão finalizada com {} termos'.format(total))

