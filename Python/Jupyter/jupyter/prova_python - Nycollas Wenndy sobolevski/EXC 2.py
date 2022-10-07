# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:41:01 2022

@author: DISRCT
"""

# tabela = {'palmeiras':30,
#           'corintians':24,
#           'fluminense':17,
#           'Vasco da gama':12}

# rodadas = int(input("Insira o numero de rodadas: "))

# for j in range(rodadas):
#     for i in tabela:
#         print(f"""\nResultado da partida para {i}\n
#             1 - vitória
#             2 - derrota
#             3 - empate
#               """)
#         resultado = int(input(''))
#         if resultado == 1:
#             tabela[i] += 3
#         elif resultado == 2 :
#             tabela[i] += 0
#         elif resultado == 3 :
#             tabela[i] += 1
#     print(tabela)
# print(f'\n\n\nO time com maior pontuação é: {max(tabela)}')
        



###############################################################################  
###############################################################################  

####################### POSSÍVEIS SOLUÇÕES ####################################  

import operator


tabela = {'palmeiras':30,
          'corintians':24,
          'fluminense':17,
          'Vasco da gama':12}

rodadas = int(input("Insira o numero de rodadas: "))
pontos = [3,0,1]

for j in range(rodadas):
    for i in tabela:
        print(f"""\nResultado da partida para {i}\n
            1 - vitória
            2 - derrota
            3 - empate
              """)
        resultado = int(input(''))
        tabela[i] += pontos[resultado-1]
        
        
        

print(f'o time com mais pontos foi o {max(tabela, key=tabela.get)} com {max(tabela.values())} pontos')      #alternativa 1
print(f'o time com mais pontos foi o {max(tabela.items(), key=operator.itemgetter(1))[0]} com {max(tabela.values())} pontos')       #alternativa 2
            