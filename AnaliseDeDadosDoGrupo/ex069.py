title = 'CADASTRE UMA PESSOA'
fim = 'FIM DO PROGRAMA'
tot18 = 0
tothomens = 0
totmulheres20 = 0
while True:
    print('-' * 25)
    print(f'{title:^25}')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totmulheres20 += 1
    print('-' * 25)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'=' * 5, f'{fim:^10}', f'=' * 5)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {tothomens} homens cadastrados')
print(f'E temos {totmulheres20} mulheres com menos de 20 anos')



