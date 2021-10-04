pessoas = {}
soma = cont = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()
    idade =  int(input('Idade: '))
    soma += idade
    pessoas['idade'] = idade
    cont += 1
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'O grupo tem {cont} pessoas.')
media = soma / cont
print(f'A media de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ')
print(f'Lista das pessoas que estão acima da média:')
for p in range(0, cont):
    if pessoas['idade'] > media:
        print(pessoas)
print('<< ENCERRADO >>')
