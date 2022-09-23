frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('O inverso de {} é {} '.format(junto, inverso))
else:
    print('A frase digitada não é um palíndromo\n TEMOS UMA PALINDROMO')
