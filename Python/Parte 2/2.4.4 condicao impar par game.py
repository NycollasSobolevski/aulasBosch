# =============================================================================
# exemplo 01 
#imprima os numeros pares de 0 a 30 usando 'for'
# for i in range(31):
#     if i%2==0:
#         print(i)
# 
# =============================================================================

# =============================================================================
# exemplo 2    
#
#h = int(input('insira a largura e altura: '))
# for i in range(h):
#     print('x '*h)
# =============================================================================

# =============================================================================
# #Exemplo 03 - serie de Fibonacci
# 
# escolha = int(input('Numero: '))
# 
# lista = [0,1]
# 
# for i in range(escolha):
#     lista.append(lista[i] + lista[i+1])
# 
# print(lista[0: escolha])
# 
# 
# # Outra forma
# # a = 0
# # b = 1
# # c = 0 
# # for i in range(escolha):
# #     print(a)
# #     c=b
# #     b+=a
# #     a=c
# =============================================================================
import random

#jogo impar ou par 
compNum = [0,1,2,3,4,5,6,7,8,9]

print("""
 #####      ##     #####              ####    ##  ##             ####    ##   ##  #####      ##     #####
 ##  ##    ####    ##  ##            ##  ##   ##  ##              ##     ### ###  ##  ##    ####    ##  ##
 ##  ##   ##  ##   ##  ##            ##  ##   ##  ##              ##     #######  ##  ##   ##  ##   ##  ##
 #####    ######   #####             ##  ##   ##  ##              ##     ## # ##  #####    ######   #####
 ##       ##  ##   ####              ##  ##   ##  ##              ##     ##   ##  ##       ##  ##   ####
 ##       ##  ##   ## ##             ##  ##   ##  ##              ##     ##   ##  ##       ##  ##   ## ##
 ##       ##  ##   ##  ##             ####     ####              ####    ##   ##  ##       ##  ##   ##  ##
 """)

while True:
    while True:
        print('\nDigite \"sair\" para sair')
        userPI = input('Impar ou par: ')
        if userPI == 'impar' or userPI=='par':
            
            userNum = int(input('Digite seu numero: '))
            random_num = random.choice(compNum)
            print('o computador jogou',str(random_num))
            result = userNum+random_num
            
            if userPI == 'impar':
                if (userNum+random_num)%2==1:
                    print(userNum,'+',random_num, '=', result,'You Win!')
                    
                else:
                    print(userNum,'+',random_num, '=', result,'You Lose')
                    
            elif userPI=='par':
                if (userNum+random_num)%2==0:
                    print(userNum,'+',random_num, '=', result,'You Win!')
                    
                else:
                    print(userNum,'+',random_num, '=', result,'You lose')
                    
            elif userPI=='sair':
                break
        elif userPI=='sair':
            break
    break

            
            
            
            
