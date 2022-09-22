print('-'*19)
print('\033[7;34mEmpréstimo Bancario\033[m')
print('-'*19)

salario = float(input('Digite seu salario: '))
valor = float(input('Qual o valor necessario? '))
anos = int(input('Em quantos anos voce pretende pagar? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar a  casa de R${:.2f} em {} anos'.format(valor, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

if prestacao >= minimo:
    print('Seu emprestimo foi \033[31mnegado\033[m')
else:
    print('\033[32mEMPRESTIMO APROVADO\033[m')



