print('-'*19)
print('Analisador de Pesos')
print('-'*19)

maior = 0
menor = 0
for i in range(1, 6):
    peso = int(input('Digite o peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso foi {}Kg\n'
      'E o Menor peso foi {}Kg'.format(maior, menor))
