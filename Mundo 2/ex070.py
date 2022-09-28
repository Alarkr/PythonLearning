print('-'*35)
print('{:^35}'.format('Lojas Kiker Magazine'))
print('-'*35)
totC = prodMil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Nome do Produto: ')).strip()
    pr = float(input('Preço: R$'))
    cont += 1
    print('='*25)
    totC += pr
    if pr >= 1000:
        prodMil += 1
    if cont == 1 or pr < menor:
        menor = pr
        barato = prod
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar comprando? [ S/N ]')).upper().strip()[0]
    if op == 'N':
        break
print('{:^35}'.format('FIM DA COMPRA'))
print(f'O total da compra foi: R${totC:.2f}')
print(f'Temos {prodMil} produtos custando mais de R$1000')
print(f'O produto mais barato foi a {barato} custando {menor:.2f}')
