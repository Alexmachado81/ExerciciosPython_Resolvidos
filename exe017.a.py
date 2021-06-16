import math
print ('Calculo da Hipotenusa')
caad = float(input('Informe o cateto adjacente :\n'))
caop = float(input('Informe o cateto oposto :\n'))
hipo = math.sqrt(math.pow(caad,2)+math.pow(caop,2))
print( ' No triangulo retangulo cujo o cateto oposto é {} e o cateto adjacente é {}, a A hipotenusa é {:.1f} '.format(caop,caad,hipo))
