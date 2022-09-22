from random import randint
from time import sleep

print('Jogo da Adivinhação')

print('-=-'*16)
print('Vou pensar um número de 0 a 5, tente adivinhar!!')
print('-=-'*16)

x = randint(0,5)
y = int(input('Digite um número: '))

print('PROCESSANDO...')
sleep(2)

if x == y:
   print('PARABÉNS!! Você venceu!!!')
else:
   print('Você Perdeu :c. Eu pensei no número {}'.format(x))

