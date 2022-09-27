from random import randint
print('-'*19)
print('Jogo da Adivinhação')
print('-'*19)

print('\033[7;34mO computador escolheu um numero entre 0 e 10\033[m')
pc = randint(1, 10)
player = 0
qtd = 0
while pc != player:
    player = int(input('Digite o numero: '))
    if pc != player:
        qtd += 1
print('O computador escolheu o numero: {}'.format(pc))
print('Voce teve {} tentativas até acertar!!'.format(qtd))

