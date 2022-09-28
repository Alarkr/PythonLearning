print('-'*12)
print('Tabuada v2.0')
print('-'*12)

n = int(input('Digite um número para ver a tabuada:'))
print('-'*12)
for i in range(1, 11):
    r = i * n
    print('{} x {:2} = {}'.format(n, i, r))
    i = i + 1
print('-' * 12)
