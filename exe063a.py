print('-*'*20)
print('        Sequência de Fibonacci')
print('-*'*20)
seq = int(input('Informe quantos termos você quer mostras? \n'))
print('-*'*20)
t1 = 0
t2 =1
print('{} - {}'.format(t1,t2),end=' ')
cont = 3
while cont <= seq:
    t3 = t1 + t2
    print('- {}'.format(t3),end=' ')
    cont += 1
    t1 = t2
    t2 = t3
print('- fim ')
print('-*'*20)


