print('=' * 35)
print('{:^41}'.format('BANCO \033[31mCV\033[m'))
print('=' * 35)

valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('VOLTE SEMPRE AO BANCO DO \033[31mCV\033[m')