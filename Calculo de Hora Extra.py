from time import sleep
print('==' * 21)
print('{:^42}'.format('Calculos Empresariais'))
print('==' * 21)

nome = str(input('Digite seu nome:')).strip().capitalize()
salBruto = float(input('Qual o seu salario? -> '))
while True:
    print(f'Olá {nome}!! \n'
          'O que voce deseja?\n'
          '[ 1 ] Calcular hora extra\n'
          '[ 2 ] Mostrar quanto Recebo por Dia e Hora\n'
          '[ 3 ] Calcular 40% do FGTS')
    op = int(input('Qual sua opção? -> '))
    print('~~' * 21)

    if op == 1:
        hMes = int(input('Quantas Horas voce trabalhou esse mes?'))
        hNor = float(input('Quantas horas 50% voce fez?-> '))
        hCem = float(input('Quantos horas 100% voce trabalhou?-> '))

        hora = salBruto / hMes
        HEN = hora * 1.5
        HEC = hora + hora

        horaExtra50 = HEN * hNor
        horaExtra100 = HEC * hCem
        totalHE = horaExtra50 + horaExtra100

        print(f'Valor da Hora normal: R${hora:.2f}')
        sleep(1)
        print(f'Valor da Hora Extra 50%: R${HEN:.2f}')
        sleep(1)
        print(f'Valor da Hora Extra 100%: R${HEC:.2f}')
        sleep(1)
        print(f'Valor de quanto vai receber Extra 50%: R${horaExtra50:.2f}')
        sleep(1)
        print(f'Valor de quanto vai receber Hora Extra 100%: R${horaExtra100:.2f}')
        sleep(1)
        print(f'O total de horas extra que voce ira receber é R${totalHE}')

    elif op == 2:
        hMes = int(input('Quantas Horas voce trabalhou esse mes?-> '))
        hDia = int(input('Quantas horas voce trabalhou nesse dia?-> '))
        hora = salBruto / hMes
        dia = hora * hDia
        print(f'{nome}, Com o salario de R${salBruto:.2f}\n'
              f'Você recebe R${dia:.2f} por dia e R${hora:.2f}/hora')
        print('~~' * 21)

    elif op == 3:
        print('{:^40}'.format('Em contrução'))
        print('~~' * 21)

    op2 = ' '
    while op2 not in 'SN':
        op2 = str(input('Deseja Realizar outra operação? [ S/N ]-> ')).upper().strip()[0]
    if op2 == 'N':
        break
print('Programa finalizado, Volte Sempre')
