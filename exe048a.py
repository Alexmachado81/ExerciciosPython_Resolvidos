s = 0
conte = 0
for c in range(1,501,2):
    if c % 3 ==0:
        s = c + s
        conte = conte + 1
print(' A soma de todos os {} dos valor impares devivados de 3 é {}'.format(conte,s))