print('-'*13)
print('Maior e menor')
print('-'*13)
maior = menor = cont = tot = media = 0
op = ''
while op in 'Ss':
    num = int(input('Digite um numero: '))
    tot += num
    cont += 1
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('Deseja continuar? [ S/N ]')).lower().strip()[0]
media = tot / cont
print(f'Voce digitou {cont} numero e a media deles foi {media}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
