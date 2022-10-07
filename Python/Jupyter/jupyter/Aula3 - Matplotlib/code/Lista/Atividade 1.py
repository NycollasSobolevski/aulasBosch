# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:11:06 2022

@author: DISRCT
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import random


valor = []

for i in range(3):
    a = random.randint(0, 50)
    valor.append(a)
    valor.sort()
    
sen = np.sin(valor)


#########################  SENO  #####################
senX = np.arange(-3,3,0.1)
senY = np.sin(senX)

fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (20,8))
eixo[0][0].plot(senX,senY, linewidth=2, label='Sen')


########################### COSSENO ##################


cosX = np.arange(-3,3,0.1)
cosY = np.cos(cosX)
eixo[0][1].plot(cosX,cosY,label='Cos')


###################### TANGENTE ######################

tanX = np.arange(-3,3,0.03)
tanY = np.tan(tanX)
eixo[1][0].plot(tanX,tanY,label='Tan')
# help(plt.plot)

plt.savefig('Atividade 1.png')
##############################################################################
##############################################################################
##############################################################################
