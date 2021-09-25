cores = {'limpa':'\033[m', 'blue':'\033[34m'}
print('=' * 30)
print('{}{:^30}{}'.format(cores['blue'], ('BANCO CEV'), cores['limpa']))
print('=' * 30)
valor = int(input('Que valor quer sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} células de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANOO CEV! Tenha um bom dia!')