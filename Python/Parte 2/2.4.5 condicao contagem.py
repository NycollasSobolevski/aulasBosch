# =============================================================================
#   Exercicio 1 
#
# #contagem 
# import time
#
#
# def cont(a,b,c):
#     if a>b:
#         for i in range(a,b-1,-c):        
#             print(i)
#             time.sleep(0.5)
#           
#     elif a<b:
#         for i in range(a,b+1,c):        
#             print(i)
#             time.sleep(0.5)
#     
#
# inicio = int(input('Digite o inicio da contagem: '))
# final = int(input('Digite o final da contagem: '))
# quanto = int(input('Digite de quanto em quanto: '))
#
# cont(inicio,final,quanto)
# =============================================================================

# =============================================================================
# 
#   Exercicio 2 
#
# import math #-------------------- biblioteca de matematica --------------------
# 
# def calculo(x):
#     print(f'Raiz quadrada de {x} = {math.sqrt(x):.2f}')
#     print(f'Quadrado de {x} = {math.pow(x, 2)}')
#     print(f'Inverso de {x} = {round(1/x, 2)}')      #round serve para arredondar o numero quando nao é inteiro, a qual '1/x' é a equação executada e '2' é o tanto de casas decimais
#     print(f'Fatorial de {x} = {math.factorial(x)}')
# 
# 
# valor = int(input('Digite um valor: '))
# calculo(valor)
# 
# =============================================================================
# =============================================================================
# 
# import random
# # aleatorio = 'random.randint(inferior,superior)'
# 
# lista = []
# ordem = []
# 
# flag = False
# 
# 
# inferior = int(input('Digite o limite inferior: '))
# superior = int(input('Digite o limite superior: '))
# tamanho = int(input('Diigite o tamanho da lista: '))
# 
# for i in range(tamanho):
#     lista.append(random.randint(inferior,superior))
# 
# ordem = lista[:]
# 
# for i in range(len(ordem)):
#     for j in range(len(ordem)):
#         if ordem[j] > ordem[i]:
#             ordem[j], ordem[i] = ordem[i], ordem[j]
#     
#     
# print('lista = ',lista)
# print('ordem = ',ordem)
# =============================================================================
#deixando a prova de erro a calculadora (try- except)
while True:
     
    resultado = 0
    
    
    while True:
        try:
            primeiro = int(input('Digite o primeiro numero: '))
            print(primeiro)
            break
        except:
            print('\nDigite um NUMERO')
        
        
    while True:
        try:
            segundo = int(input('Digite o segundo numero: '))
            print(segundo)
            break
        except:
            print('\nDigite um NUMERO')
          
    
    
    while True:
        print('''operações:
          1 - soma
          2 - Subtração
          3 - Multiplicação
          4 - Divisão
          5 - Sair''')
        operacao =int(input('Digite a operação desejada: '))
        print(operacao)
        if operacao == 1 :
            print('resultado =',primeiro+segundo)
            break
        if operacao == 2 :
            print('resultado =',primeiro-segundo)
            break
        if operacao == 3:
            print('resultado =',primeiro*segundo)
            break
        if operacao == 4 :
            print('resultado =',primeiro/segundo)
            break
        if operacao == 5 :
            break
        else:
            print('Digite um valor numerico')
    if operacao == 5:
        print('Turn Off')
        break
