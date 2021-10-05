def area(larg, comp):
    a = l * c
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# Programa principal
print('  Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

