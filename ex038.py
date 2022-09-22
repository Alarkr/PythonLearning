print('Comparando numeros')
print('-'*18)

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O \033[34mPrimeiro valor\033[m é \033[1;32mmaior')
elif n2 > n1:
    print('O \033[34mSegundo valor\033[m é \033[1;32mmaior')
else:
    print('\033[4;34mNão existe Valor maior. \033[1;32m{} e {} são iguais'.format(n1, n2))
