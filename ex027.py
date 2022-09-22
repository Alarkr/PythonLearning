print('Primeiro e Último')
print('-'*17)

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print('Muito Prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
