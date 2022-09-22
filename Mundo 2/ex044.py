print('-'*25)
print('Gerenciador de Pagamentos')
print('-'*25)

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO \n[ 1 ]à vista dinheiro/pix \n[ 2 ] à vista cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    precoF = preco - (preco * 0.10)
    print('Sua compra à vista no dinheiro ou pix tem 10% de Desconto!')
    print('O preço a ser pago é R${}'.format(precoF))
elif opcao == 2:
    precoF = preco - (preco * 0.05)
    print('Sua compra à vista no cartão tem 5% de Desconto!')
    print('O preço a ser pago é R${}'.format(precoF))
elif opcao == 3:
    precoF = preco / 2
    print('Sua compra em 2x no cartão serão em duas parcelas de R${}'.format(precoF))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas?'))
    precoF = preco + (preco * 0.20)
    precoP = (preco + (preco * 0.20)) / parcelas
    print('Sua compra será parcelada em {}x de R${} COM JUROS de 20%'.format(parcelas, precoP))
    print('Sua compra de R${} vai custar R${} no final'.format(preco,  precoF))
