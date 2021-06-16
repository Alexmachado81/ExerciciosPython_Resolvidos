import math

angulo = float(input('informe o angulo que voce deseja: \n'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print (' O valor de seno para o angulo de {} é :{:.2f}'.format(angulo,seno))
print (' O valor de coseno para o angulo de {} é :{:.2f}'.format(angulo,coseno))
print (' O valor da tangente para o angulo de {} é :{:.2f}'.format(angulo,tangente))
