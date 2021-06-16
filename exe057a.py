sexo = str(input("Informe seu sexo (M/F): ")).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input("Dados invalidos. Informe seu sexo (M/F): ")).upper().strip()[0]
print(' sexo {} registrado com sucesso!'.format(sexo))
