from math import floor

print('PORÇÃO INTEIRA')
print('-'*14)

n = float(input('Digite um valor decimal:'))

print('O valor {} tem a parte inteira: {}'.format(n, floor(n)))
