print('ANALISADOR DE TEXTO')
print('-'*19)

nome = str(input('Digite seu nome completo:')).strip()

print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: ' + nome.upper())
print('Seu nome em letras minúsculas é: ' + nome.lower())
print('Seu nome todo tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
