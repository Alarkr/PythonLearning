print('Verificador de String')
print('-'*21)

frase = str(input('Digite um frase: ')).upper().strip()

print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
