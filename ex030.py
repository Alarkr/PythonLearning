print('Multa de Trânsito')
print('-'*17)

v = float(input('Qual velocidade o carro passou? '))

if v >= 80:
   print('Você foi  multado. O valor da multa é: R${}'.format((v-80)*7))
else:
   print('Bom trabalho, continue no limite de velocidade!!')