print('Par ou Ímpar')
print('-'*13)

n = int(input('Digite um número: '))

if n % 2 == 1:
   print('{} é um número ÍMPAR!'.format(n))
else:
   print('{} é um número PAR'.format(n))
