print('Desconto em produtos')
print('-'*20)

p = float(input('Digite o valor do produto:'))
d = p * (5/100)
df = p - d

print('O valor do produto com 5% de desconto é {}'.format(df))