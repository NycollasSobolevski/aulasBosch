# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:22:34 2022

@author: disrct
"""
import numpy as np


matriz = np.random.randint(0,10,(5,5))
print(matriz)

numeros =[]

impar = (matriz%2 != 0)
numeros.append(matriz[impar])
matriz[impar] = matriz[impar]**2 

print('\n\n',matriz)
# print("\n",numeros)
print(f'\nExistem {len(numeros[0])} registros.')
