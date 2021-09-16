from random import randint
from time import sleep
cores = {'limpa':'\033[m', 'blue':'\033[34m', 'red':'\033[31m', 'yellow':'\033[33m', 'magenta':'\033[35m', 'green':'\033[32m'}
negrito = {'bold':'\033[1m'}
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ {}{}0{} ] PEDRA
[ {}{}1{} ] PAPEL
[ {}{}2{} ] TESOURA'''.format(cores['magenta'], negrito['bold'], cores['limpa'], cores['magenta'], negrito['bold'],
                              cores['limpa'], cores['magenta'], negrito['bold'], cores['limpa']))
jogador = int(input('Qual a sua jogada? '))
if jogador > 2:
    print('{}JOGADA INVÁLIDA!{}'.format(cores['red'], cores['limpa']))
else:
    print('{}JO{}'.format(cores['green'], cores['limpa']))
    sleep(1)
    print('{}KEN{}'.format(cores['green'], cores['limpa']))
    sleep(1)
    print('{}PO!!!{}'.format(cores['red'], cores['limpa']))
    print('-=' * 11)
    print('{}Computador{} jogou {}'.format(cores['yellow'], cores['limpa'], itens[computador]))
    print('{}Jogador{} jogou {}'.format(cores['blue'], cores['limpa'], itens[jogador]))
    print('-=' * 11)
    if computador == 0: # computador jogou PEDRA
        if jogador == 0:
            print('{}EMPATE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 1:
            print('{}JOGADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 2:
            print('{}COMPUTADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
    elif computador == 1: # computador jogou PAPEL
        if jogador == 0:
            print('{}COMPUTADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 1:
            print('{}EMPATE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 2:
            print('{}JOGADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
    elif computador == 2: # computador jogu TESOURA
        if jogador == 0:
            print('{}JOGADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 1:
            print('{}COMPUTADOR VENCE{}'.format(negrito['bold'], cores['limpa']))
        elif jogador == 2:
            print('{}EMPATE{}'.format(negrito['bold'], cores['limpa']))

