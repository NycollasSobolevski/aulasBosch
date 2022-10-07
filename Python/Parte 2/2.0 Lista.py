#lista
#crie uma lista com 10 valores
#peça ao usuario escolher os 10 valores
#Mostre os valores
#Mostre a lista ordenada

lista = []                                      # aqui se cria uma lista vazia
escolha = int(input('Escolha um valor 1: '))    # aqui se solicita que digite um valor para entrar
lista.append(escolha)                            #'.append' adiciona o valor ('escolha') à variavel 'lista'
escolha = int(input('Escolha um valor 2: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 3: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 4: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 5: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 6: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 7: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 8: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 9: '))
lista.append(escolha)
escolha = int(input('Escolha um valor 10: '))
lista.append(escolha)
lista.sort()                                            #'.sort()' ordena a lista, na qual ela entra em sequencia
print('\nQuantos itens tem na lista:',len(lista))       #'len' e o comando para contar quantos valores há na lista
print(lista)
