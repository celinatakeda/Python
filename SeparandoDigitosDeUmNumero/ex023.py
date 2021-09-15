cores = {'limpa':'\033[m', 'green':'\033[32m', 'yellow':'\033[33m', 'red':'\033[31m', 'blue':'\033[34m'}
negrito = {'bold':'\033[1m'}
num = int(input('Informe um número: '))
print('Analisando o número: {}{}{}'.format(negrito['bold'], num, cores['limpa']))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}{}{}'.format(cores['yellow'], u, cores['limpa']))
print('Dezena: {}{}{}'.format(cores['blue'], d, cores['limpa']))
print('Centena: {}{}{}'.format(cores['red'], c, cores['limpa']))
print('Milhar: {}{}{}'.format(cores['green'], m, cores['limpa']))
