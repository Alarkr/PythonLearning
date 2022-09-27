print('-'*19)
print('Calculo de Fatorial')
print('-'*19)
''' Utilizando modulo
from math import factorial
n = int(input('Digite um numero para\ncalcular seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n, f))'''

'''Modo convencional'''

n = int(input('Digite um numero para\ncalcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
