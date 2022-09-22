print('BOAS VINDAS')
nome = input('Digite seu nome:').capitalize()
cores = {
    'limpa':'\033[m',
    'verde':'\033[32m',
    'branco':'\033[30m'
}
print('É um prazer te conhecer {}{}!{}'.format(cores['verde'], nome, cores['limpa']))
