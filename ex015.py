print('ALUGUEL DE CARROS')
print('-'*17)

d = float(input('Quantos dias de aluguel?'))
k = float(input('Quantos KM rodados?'))
vt = (d * 60.00) + (k * 0.15)

print('O valor total a ser pago é R${}'.format(vt))