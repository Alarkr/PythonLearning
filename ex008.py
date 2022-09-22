print('Conversão de medidas')
print('-'*20)

m = float(input('Digite a distacia em metros para conversão:'))

k = m * 1000
h = m * 100
da = m * 10
dm = m / 10
cm = m / 100
mm = m / 1000

print('Tabela de medidas')
print('|KM {} | HM {} | DAM{} | M{}| DM {} | CM {} | MM {}|'.format(k, h, da, m, dm, cm, mm))
