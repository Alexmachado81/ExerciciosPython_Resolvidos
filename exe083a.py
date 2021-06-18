frase = str(input('Digite uma expressão:'))
print(frase)
esq = dir =0
for simb in frase:
    if simb == ')':
        dir += 1
    elif simb == '(':
        esq +=1
if dir == esq:
    print('Sua espressão esta valida')
else:
    print('Sua expressão esta invalida')
