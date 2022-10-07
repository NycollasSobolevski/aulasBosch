#cardapio

cardapio = {
            'hamburguer':10.00,
            'hotdog':6.50,
            'salada':4.00,
            'suco':4.00,
            'refrigerante':4.50,
            'agua':2.00
            }

for i in cardapio:   
    print(i, cardapio[i])

selecao = input('Que comida deseja?')
print(cardapio[selecao])
selecao2 = input('Que bebida deseja?')
print(cardapio[selecao2])
print('\nTOTAL:',cardapio[selecao]+cardapio[selecao2])
