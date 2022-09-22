print('\033[7;34mIMC\033[m')

peso = float(input('Quanl é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (M)'))
imc = peso / altura ** 2

print('Seu IMC é {:.1f}'.format(imc))
if imc < 16:
    print('Magreza Grave')
elif imc < 17:
    print('Magreza Moderada')
elif imc < 18.5:
    print('Magreza Leve')
elif imc < 25:
    print('Saudavel')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')
