import math

frase = math.pi
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('O inverso de {} é {} '.format(junto, inverso))
else
    print('A frase digitada não é um palíndromo')

