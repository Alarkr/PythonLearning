print('-'*12)
print('Tabuada v3.0')
print('-'*12)
cont = 0
while True:
    n1 = int(input('Digite um número para ver a tabuada: '))
    print('-' * 35)
    if n1 < 0:
        break

    for c in range(1, 11):

        r = c * n1
        print(f'{n1} x {c} = {r}')
        c += 1
    print('-'*35)
print('PROGRAMA FINALIZADO...')
