print('-'*13)
print('Gerador de PA')
print('-'*13)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
