print('-'*19)
print('10 TERMOS DE UMA PA')
print('-'*19)

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao

for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i), end=', ')
print('ACABOU')
