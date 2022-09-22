from random import randint
from time import sleep
import os
import sys

print('-' * 11)
print('Jan Ken Pon')
print('-' * 11)

itens = ('Pedra', 'Papel', 'Tesoura')
maquina = randint(0, 2)

print('Suas Opções '
      '\n[ 0 ] PEDRA '
      '\n[ 1 ] PAPEL '
      '\n[ 2 ] TESOURA')
jogador = int(input('Qual sua jogada? '))

print('JAN')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=' * 13)
print('O Jogador escolheu {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[maquina]))
print('-=' * 13)

if maquina == 0:  # Computador jogou Pedra
    if jogador == 0:  # Pedra
        print('\033[33mEmpate!\033[m')
    elif jogador == 1:  # Papel
        print('\033[34mJogador VENCEU!!\033[m')
    elif jogador == 2:  # Tesoura
        print('\033[31mComputador VENCEU!! \033[m')
    else:
        print('Jogada invalida')
elif maquina == 1:  # Computador jogou Papel
    if jogador == 0:  # Pedra
        print('\033[31mComputador VENCEU!! \033[m')
    elif jogador == 1:  # Papel
        print('\033[33mEmpate!\033[m')
    elif jogador == 2:  # Tesoura
        print('\033[34mJogador VENCEU!!\033[m')
    else:
        print('Jogada invalida')

elif maquina == 2:  # Computador jogou Tesoura
    if jogador == 0:  # Pedra
        print('\033[34mJogador VENCEU!!\033[m')
    elif jogador == 1:  # Papel
        print('\033[31mComputador VENCEU!! \033[m')
    elif jogador == 2:  # Tesoura
        print('\033[33mEmpate!\033[m')
    else:
        print('Jogada invalida')


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


print('Jogar novamente? \n[ 1 ] Sim \n[ 2 ] Não')
x = int(input('Sua Opção: '))
if x == 1:
    os.system('cls') or None
    restart_program()
else:
    exit()
