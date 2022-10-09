from time import sleep

print('==' * 21)
print('{:^42}'.format('Calculos Empresariais'))
print('==' * 21)

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip().lower()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO: Digite um valor valido.\033[m')
        if ok:
            break
    return (valor)


def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isdecimal():
            valor = float(n)
            ok = True
        else:
            print('\033[0;31mERRO: Digite um valor valido.\033[m')
        if ok:
            break
    return (valor)


nome = str(input('Digite seu nome:')).strip().capitalize()
salBruto = leiaFloat('Qual o seu salario? -> ')
while True:
    print(f'Olá {nome}!! \n'
          'O que voce deseja?\n'
          '[ 1 ] Calcular hora extra\n'
          '[ 2 ] Mostrar quanto Recebo por Dia e Hora\n'
          '[ 3 ] Calcular 40% do FGTS')
    op = leiaInt('Qual sua opção? -> ')
    print('~~' * 21)

    if op == 1:
        hMes = 220
        hNor = leiaFloat('Quantas horas 50% voce fez?-> ')
        hCem = leiaFloat('Quantos horas 100% voce trabalhou?-> ')

        hora = salBruto / hMes
        HEN = hora * 1.5
        HEC = hora + hora
        horaExtra50 = HEN * hNor
        horaExtra100 = HEC * hCem
        totalHE = horaExtra50 + horaExtra100

        print(f'Valor da 1 Hora Extra 50%: \033[34mR${HEN:.2f}\033[m\n'
              f'Valor da 1 Hora Extra 100%: \033[34mR${HEC:.2f}\033[m')
        sleep(1)
        print(f'Total de Horas Extras 50%: \033[34mR${horaExtra50:.2f}\033[m\n'
              f'Total de Horas Extras 100%: \033[34mR${horaExtra100:.2f}\033[m')
        sleep(1)
        print(f'O total de horas extra que voce ira receber é \033[34mR${totalHE:.2f}\033[m')
        print(f'--Salario mais Horas Extras--\n'
              f'\033[34m{salBruto:.2f} + {totalHE:.2f} = {salBruto + totalHE:.2f}\033[m')
        print('~~' * 21)

    elif op == 2:
        hDia = int(input('Quantas horas voce trabalhou nesse dia?-> '))
        print('Considerando 220 horas trabalhadas')
        hora = salBruto / 220
        dia = hora * hDia
        print(f'{nome}, Com o salario de R${salBruto:.2f}\n'
              f'Você recebe R${dia:.2f} por dia e R${hora:.2f}/hora')
        print('~~' * 21)

    elif op == 3:
        anos = leiaInt('Quantos anos voce trabalha nessa empresa? ->')
        q = leiaInt('Voce irá receber 40% na demissão?\n'
                    '[ 1 ] Sim\n'
                    '[ 2 ] Não\n'
                    'Sua Opção -> ')
        fgts = salBruto * 0.08
        fgtsMeses = anos * 12
        totFgts = fgtsMeses * fgts
        fgts40 = totFgts + (totFgts * 0.4)
        print(f'{nome}, voce recebe R${fgts:.2f} de fgts por mês')
        if q == 1:
            print(f'Trabalhando na empresa por {anos} anos,\n'
                  f'e recebendo 40% da empresa'
                  f'voce tem direito receber R${fgts40:.2f} de FGTS')
        elif q == 2:
            print(f'Trabalhando na empresa por {anos} anos,\n'
                  f'voce tem direito receber R${totFgts:.2f} de FGTS')
        print('~~' * 21)

    op2 = leiaInt('Deseja Realizar outra operação?\n'
                  '[ 1 ] Sim\n'
                  '[ 2 ] Não\n'
                  'Sua Opção-> ')
    if op2 == 2:
        break
print('\n\033[31mPrograma finalizado, Volte Sempre\033[m')
