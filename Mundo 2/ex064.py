print('-'*21)
print('Digite 999 para parar')
print('-'*21)
x = cont = tot = 0
x = int(input('Digite um numero: '))
while x != 999:
    tot += x
    cont += 1
    x = int(input('Digite um numero: '))
print('Voce digitou {} numeros'.format(cont))
print('A soma entre eles foi {}'.format(tot))
