lista = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze'
         ,'doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Informe um numero entre [0 e 20]'))
    if 0<= num <=20:
        break
    print('Tente novamente,',end=" ")
print(f'O numero escolhido foi {lista[num]}')


