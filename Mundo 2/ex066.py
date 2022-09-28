print('-'*21)
print('Digite 999 para parar')
print('-'*21)
cont = soma = 0
while True:
    x = int(input('Digite um numero: '))
    if x == 999:
        break
    cont += 1
    soma += x
print(f'Vode digitou {cont} vezes \nA soma dos numero é {soma}')
