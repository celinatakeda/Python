from time import sleep
opcao = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while opcao != 5:
    print('''    [ 1 ]somar
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ]novos números
    [ 5 ]sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = v1 + v2
        print(f'A soma entre {v1} + {v2} é {soma}')
    elif opcao == 2:
        produto = v1 * v2
        print(f'O resultado de {v1} x {v2} é {produto}')
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'Entre {v1} e {v2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opçcão inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

