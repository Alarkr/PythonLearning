print('Conversor de Bases')
print('-' * 18)

n = int(input('Digite um numero inteiro: '))

print('Escolha uma das bases para conversão \n[ 1 ] Converter para BINARIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL \n[ 4 ] Sair')
op = int(input('Sua Opção: '))

if op == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
elif op == 4:
    exit()
else:
    print('Opção invalida. Tente novamente')

