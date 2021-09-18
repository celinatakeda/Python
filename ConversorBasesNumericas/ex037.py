cores = {'limpa':'\033[m', 'azul':'\033[34m'}
num = int(input('Digite um número inteiro: '))
print('-=-' * 13)
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
print('-=-' * 13)
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print('{}{}{} convertido para HEXADECIMAL é igual a {}'.format(cores['azul'], num, cores['limpa'], hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')