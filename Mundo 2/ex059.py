from time import sleep
print('-' * 24)
print('Menu de opções- Calculos')
print('-' * 24 + '\n')

n1 = int(input('Digite o Primeiro numero: '))
n2 = int(input('Digite o Segundo numero: '))
x = 0
while x != 5:
    print('O que voce deseja?\n'
          '[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Numero maior\n'
          '[ 4 ] Novos numeros\n'
          '[ 5 ] Sair\n')
    x = int(input('Sua opção: '))
    print('='*22)
    if x == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
        print('=' * 22)
    elif x == 2:
        mult = n1 * n2
        print('{} + {} = {}'.format(n1, n2, mult))
        print('=' * 22)
    elif x == 3:
        if n1 > n2:
            print('O primeiro numero é maior que o segundo')
            print('--- {} > {} ---'.format(n1, n2))
        elif n2 > n1:
            print('O segundo numero é maior que o primeiro')
            print('--- {} < {} ---'.format(n1, n2))
        elif n1 == n2:
            print('O primeiro numero é IGUAL ao segundo')
            print('--- {} = {} ---'.format(n2, n1))
        print('=' * 22)
    elif x == 4:
        print('Informe os numeros novamente!')
        n1 = int(input('Digite o Primeiro numero: '))
        n2 = int(input('Digite o Segundo numero: '))
        print('=' * 22)
    elif x == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida. Tente novamente')
        print('=' * 22)
    sleep(2)
print('Fim do programa. Volte sempre!!')
