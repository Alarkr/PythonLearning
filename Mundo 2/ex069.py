tot18 = totH = totM = 0
while True:
    print('='*29)
    print('Cadastre uma pessoa')
    print('='*29)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [ M/F ]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo == 'F':
        totM += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if op == 'N':
        break


print(f'Total de pessoas maiores de 18: {tot18}')
print(f'ao todo temos {totH} homem cadastrados ')
print(f'E temos {totM} mulher com menos de 20 anos')
print('='*29)
print('Programa finalizado')
