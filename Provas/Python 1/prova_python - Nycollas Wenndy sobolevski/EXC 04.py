# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:06:29 2022

@author: DISRCT
"""

alunos = {'miguel':0,
         'angelo':0,
         'isaquiel':0,
         'matheus':0
         }

gabarito = ['a','c','b','e','a','a','c','b','d','d']
questoes = [1,2,3,4,5,6,7,8,9,10]
erro = []


for i in range(10):
    resposta = input(f'Qual a sua resposta para a questão {i+1}? ')
    if resposta != gabarito[i]:
        erro.append(i+1)
    
    
print(f'Voce errou a(s) questão(ões): {erro}')