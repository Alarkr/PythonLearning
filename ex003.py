print('\033[31mSOMA')
print('-'*4, '\033[m')

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1+n2
cores = {'branco':'\033[30m',
         'vermelho':'\033[31m',
         'limpa':'\033[m'}

print('A soma entre {}{} e {} é: {}!{}'.format(cores['vermelho'], n1, n2, s, cores['limpa']))
