print('-'*14)
print('Numeros Primos')
print('-'*14)

num = int(input('Digite um numero: '))
tot = 0
for i in range(1, num + 1, 1):
    if num % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[33m',end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {}, foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
