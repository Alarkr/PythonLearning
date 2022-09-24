from datetime import date

print('-'*19)
print('Analisador de nomes')
print('-'*19)
anoAtual= date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pessoa)))
    idade = anoAtual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade '
      '\nE tivemos {} pessoas menores de idade'.format(totmaior, totmenor))
