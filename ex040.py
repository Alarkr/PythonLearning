print('Media Escolar')
print('-'*13)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2

print('Sua média é {:.2f}'.format(media))

if media >= 7.0:
    print('\033[32mAPROVADO!!!')
elif media < 5:
    print('\033[31mREPROVADO')
elif media <= 5.0:
    print('\033[33mRECUPERAÇÃO')
