soma = cont =0

while True:
    numero = int(input('Informe um numero inteiro[digite 999 para ele parar ]:'))
    if numero == 999:
        break
    soma = soma + numero
    cont += 1
print(f' A soma dos {cont} numeros digitador é {soma}')
