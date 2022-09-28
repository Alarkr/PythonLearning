from random import randint
print('-'*12)
print('Par ou Impar')
print('-'*12)
pc = randint(0, 10)
vitoria = 0
op = int(input('O que voce deseja?\n[ 1 ] PAR\n[ 2 ] IMPAR\nDigite sua opção: '))
print('-'*20)
while True:
    jogador = int(input('Digite o numero:'))
    print('~'*20)
    resultado = pc + jogador
    if resultado % 2 == 0 and op == 1: # jogador escolhe PAR e GANHA
        print(f'O computador lançou {pc}\nO Jogador lançou {jogador}\n{resultado} é PAR\nJOGADOR GANHOU')
        print('~' * 20)
        vitoria += 1
    elif resultado % 2 == 1 and op == 1: # jogador escolhe PAR e PERDE
        print(f'O computador lançou {pc} e o Jogador lançou {jogador}\n{resultado} é IMPAR\nJOGADOR PERDEU')
        break
    elif resultado % 2 == 1 and op == 2: # jogador escolhe IMPAR e GANHA
        print(f'O computador lançou {pc} e o Jogador lançou {jogador}\n{resultado} é IMPAR\nJOGADOR GANHOU')
        print('~' * 20)
        vitoria += 1
    elif resultado % 2 == 0 and op == 2: # jogador escolhe IMPAR e PERDE
        print(f'O computador lançou {pc} e o Jogador lançou {jogador}\n{resultado} é PAR\nJOGADOR PERDEU')
        break
print(f'Voce venceu {vitoria} vezes')