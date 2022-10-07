# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:38:31 2022

@author: disrct
"""
import random
# import collections
# from iteration_utils import duplicates

tupla = tuple(random.sample(range(0,10), 5))
repeat = 0

print (tupla)

print(f'valor maximo: {max(tupla)}')
print(f'valor mínimoo: {min(tupla)}')

for i in tupla:
    if i == 5:
        repeat += 1
        
print(f'o valor 5 apareceu {repeat} vezes')

x=int(input('numero'))      #valor que vai ser procurado dentro da tupla 

if x in tupla:
    print(f'o primeiro valor {x} apareceu na posição {tupla.index(x)}')