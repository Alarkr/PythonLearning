print('-'*22)
print('Sequencia de Fibonacci')
print('-'*22)
n = int(input('Quantos termos quer mostras? '))
t1 = 0
t2 = 1
print('~'*30)
print('{}-> {}-> '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    cont += 1
    t1 = t2
    t2 = t3
    print('{}-> '.format(t3), end='')
print('FIM')
print('~'*30)
