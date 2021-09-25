cores = {'limpa':'\033[m', 'red':'\033[31m'}
total = totmil = menor = cont = 0
barato = ''
print('-' * 30)
print('{}{:^30}{}'.format(cores['red'], 'LOJA SUPER BARATÃO', cores['limpa']))
print('-' * 30)
while True:
    produto = str(input('Nome produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        barato = produto
        menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${total:.2f} ')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')


