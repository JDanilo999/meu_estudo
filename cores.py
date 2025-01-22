cores = {
    'red':'\033[1;31;40m',
    'green':'\033[4;32;40m',
    'yellow':'\033[7;33;40m',
    'blue':'\033[0;34;40m',
    'roxo':'\033[35m',
    'ciano':'\033[36m',
    'cinza':'\033[37m',
}
print('{} ola red, com fundo branco e com estilo bold.{}'.format(cores['red'],'\033[m'))
print('{} ola green, com fundo branco e com estilo underline. {}'.format(cores['green'],'\033[m'))
print('{} ola yellow, com fundo branco e com estilo negativo. {}'.format(cores['yellow'],'\033[m'))
print('{} ola blue, com fundo branco e sem nenhum estilo. {}'.format(cores['blue'],'\033[m'))
print('{} ola roxo'.format(cores['roxo']))
print('{} ola ciano'.format(cores['ciano']))
print('{} ola cinza'.format(cores['cinza']))
