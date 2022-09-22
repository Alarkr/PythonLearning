print('DISSECANDO PALAVRAS')
print('-'*19)

n = input('Digite Algo:')

print('O tipo desse valor é {}'.format(type(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Está capitalizada? {}'.format(n.istitle()))
