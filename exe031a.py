viagem = int(input(" Informe qual a distância, em quilometros, que voce predende viajar: \n"))

if viagem <= 200:
    custo1=(viagem*0.5)
    print(' Para percorer esta distância de {} quilometros, você ira gastar {:.2f} reais'.format(viagem,custo1))
else:
    custo2=(viagem*0.45)
    print(' Para percorer esta distância de {} quilometros, você ira gastar {:.2f} reais'.format(viagem,custo2))