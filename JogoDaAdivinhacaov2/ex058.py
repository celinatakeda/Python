from random import randint
cores = {'limpa': '\033[m', 'red':'\033[31m', 'yellow':'\033[33m'}
cont = 0
computador = randint(0, 10) # Faz o computador "PENSAR"
print('Sou seu computador...')
print('Acabei de  pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? ')) # JOGADOR tenta adivinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('{}Mais{}... Tente mais uma vez.'.format(cores['red'], cores['limpa']))
        else:
            print('{}Menos{}... Tente mais uma vez.'.format(cores['yellow'], cores['limpa']))
print(f'Acertou com {palpites} tentativas. Parabéns!')
