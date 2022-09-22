print('Entao viaja de avião')
print('-'*20)

viagem = float(input('Qual a distancia da viagem? '))

if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45

print('O valor da sua passagem é de R${}'.format(preco))
