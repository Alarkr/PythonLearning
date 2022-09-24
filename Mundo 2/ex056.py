print('-'*20)
print(' ANALISADOR COMPLETO')
print('-'*20)

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for i in range(1, 5):
    print('------{} Pessoa------'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1

mediaIdade = idade / 4
print('A media de idade do grupo é de {} anos'.format(mediaIdade))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))