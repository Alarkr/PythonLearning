from datetime import date
print('Alistamento Militar')


dtAtual = date.today().year
dtNasc = int(input('Digite seu ano de nascimento: '))
idade = dtAtual - dtNasc

if idade == 18:
    print('Voce deve se Alista \033[32mIMEDIATAMENTE!!!')
elif idade < 18:
    prazo = idade - 18
    print('Ainda faltam {} anos para o alistamento'.format(prazo))
    alist = dtAtual + prazo
    print('Seu alistamento será em {}'.format(alist))
elif idade > 18:
    prazo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(prazo))
    alist = dtAtual - prazo
    print('Seu alistamento foi em {}'.format(alist))
