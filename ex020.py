from random import shuffle

print('PROFESSOR 2')
print('-'*11)

n1 = str(input('Digite o nome do 1° aluno: '))
n2 = str(input('Digite o nome do 2° aluno: '))
n3 = str(input('Digite o nome do 3° aluno: '))
n4 = str(input('Digite o nome do 4° aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A orgem de apresentação seré:')
print(lista)
