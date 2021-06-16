num = int(input('Digite um numero para ver sua tabuada: \n'))
conta = 0

print('-.'*25)
for c in range(0,10):
    conta = conta +1
    mult = conta*num
    print(' \033[0;31;40m {:.1f} x {:.1f} = {}  \033[m'.format(conta,num,mult))
print('-.'*25)