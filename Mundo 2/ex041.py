from datetime import date
print('Classificando Atletas')
print('-'*21)

nasc = int(input('Ano de Nascimento'))
atual = date.today().year
idade = atual - nasc

print('O atleta tem {} anos!'.format(idade))

if idade <= 9:
    print('Classificação: Mirim! ')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <=25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')
