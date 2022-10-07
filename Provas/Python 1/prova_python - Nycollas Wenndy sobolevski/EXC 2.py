# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:41:01 2022

@author: DISRCT
"""

tabela = {'palmeiras':30,
          'corintians':24,
          'fluminense':17,
          'Vasco da gama':12}

rodadas = int(input("Insira o numero de rodadas: "))

for j in range(rodadas):
    for i in tabela:
        print(f"""Resultado da partida para {tabela[i]}
              1 - vitória
              2 - derrota
              3 - empate
              """)
        resultado = int(input(''))
        if resultado == 1:
            tabela[i] += 3
        elif resultado == 2 :
            tabela[i] += 0
        elif resultado == 3 :
            tabela[i] += 1
    print(tabela)
print(f'O time com maior pontuação é: {max(tabela)}')
        
        
    
