from random import randint
cores = {'limpa':'\033[m', 'red':'\033[31m', 'green':'\033[32m'}
print('=-' * 20)
print('{}{:^35}{}'.format(cores['red'], 'VAMOS JOGAR PAR OU ÍMPAR', cores['limpa']))
print('=-' * 20)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('{}Você VENCEU!{}'.format(cores['green'], cores['limpa']))
            v += 1
        else:
            print('{}Você PERDEU!{}'.format(cores['red'], cores['limpa']))
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('{}Você VENCEU!{}'.format(cores['green'], cores['limpa']))
            v += 1
        else:
            print('{}Você PERDEU!{}'.format(cores['red'], cores['limpa']))
            break
        print('Vamos jogar novamente...')
        print('=-' * 20)
print(f'GAME OVER! Você venceu {v} vez(es).')






