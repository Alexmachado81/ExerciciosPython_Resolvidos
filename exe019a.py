import random

print('Sorteio de aluno para colaborar com limpeza do quadro \n\n\n')

aluno1 = str(input('informe o nome de um aluno: \n'))
aluno2 = str(input('informe o nome de outro aluno: \n'))
aluno3 = str(input('informe o nome de mais um aluno: \n'))
aluno4 = str(input('informe o nome do ultimo aluno: \n'))

lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = random.choice(lista)

print('O aluno escolhido foi : {}'.format(escolhido))


