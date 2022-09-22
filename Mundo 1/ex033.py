print('Maior ou Menor')
print('-'*14)

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

#Verificando quem é menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando quem é maior
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))