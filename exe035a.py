print('='*25)
print(' Analisando um triãngulo ')
print('='*25)
ladoa = int(input('\033[0;31;40m Informe o comprimento de uma reta:\033[m \n'))
ladob = int(input('\033[0;31;40m Informe o comprimento de outra reta:\033[m \n'))
ladoc = int(input('\033[0;31;40m Informe o comprimento de mais uma reta:\033[m \n'))

if ladoa < ladob + ladoc and ladob < ladoc + ladoa and ladoc < ladoa + ladob and ladoa == ladob == ladoc:
    print ('As retas informadas formam um triangulo retangulo do tipo Equilátero')
elif ladoa < ladob + ladoc and ladob < ladoc + ladoa and ladoc < ladoa + ladob and (ladoa == ladob or ladob == ladoc or ladoa == ladoc):
    print ('As retas informadas formam um triangulo retangulo do tipo Isóceles')
elif ladoa < ladob + ladoc and ladob < ladoc + ladoa and ladoc < ladoa + ladob and ladoa != ladob != ladoc:
    print ('As retas informadas formam um triangulo retangulo do tipo Escaleno')
else:
    print('As retas informadas não formam um triangulo retangulo')