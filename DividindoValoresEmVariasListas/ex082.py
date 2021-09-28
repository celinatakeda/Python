numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
