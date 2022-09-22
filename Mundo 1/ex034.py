print('Aumento de trabalho')
print('-'*19)

s = float(input('Digite o salario: '))

if s <= 1250:
    a = s + (s * 15/100)
else:
    a = s + (s * 10/100)

print('O salario de {}, com aumento passa a ser {}'.format(s, a))
