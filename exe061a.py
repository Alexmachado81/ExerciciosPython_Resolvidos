num = int(input('Informe o primeiro termo:'))
razao = int(input('Informe a razão:'))
con =0
termo = num

while con<=10:
    termo = termo+razao
    con +=1
    print(" {} -".format(termo),end=" ")
print(" fim ")