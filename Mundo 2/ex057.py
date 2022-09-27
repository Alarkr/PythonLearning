print('-'*23)
print('Desculpa Belle Bellinha')
print('-'*23)

x = ''
while x != 'M' and 'F':
    sexo = str(input('Digite o sexo que voce se \nidentifica dentre as opções [ M/F ]: ')).upper()
    if sexo == 'M':
        print('Entendi, voce se identifica com o sexo Masculino')
        exit()
    elif sexo == 'F':
        print('Entendi, voce se identifica com o sexo Feminino')
        exit()
    else:
        print('Digite uma opção valida!\n')

