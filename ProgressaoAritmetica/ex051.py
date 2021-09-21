print('=' * 25)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print('=' * 25)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c} ', end='-> ')
print('ACABOU')
