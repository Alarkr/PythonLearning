from math import hypot

print('HIPOTENUSA')
print('-'*10)

co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hi = hypot(co, ca)

print('O valor da hipotenuza é {:.2f}'.format(hi))
