# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:17:55 2022

@author: DISRCT
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math



# # pontos = []
# pontos = [9, 12, 11, 17, 3, 4, 2, 15, 14, 2, 15, 8, 11, 16, 1, 12, 20, 11, 3, 5]
# x = []
# media = []
# media1 = media[0]
# # for i in range (20):
#     # pontos.append(random.randint(0,20))

# for i in range(len(pontos)):
#     x.append(i)
# for i in range(len(pontos)):
#     media.append(sum(pontos)/len(pontos))

# lMax = np.full(media[0] + media1.std())
# # lmin = media + y.std()

# # media = sum(pontos)/len(pontos)

# print(pontos)
# print(x)
# print(media)

# plt.plot(x,pontos, color="black")
# # help(plt.plot)
# plt.plot(x,media)
# plt.plot(x,lMax)


x = np.arange(100)
y = np.random.rand(100)

med = np.full(len(x),y.mean())
mMax = np.full(len(x),y.mean() + y.std())
mMin = np.full(len(x),y.mean() - y.std())

plt.plot(x,y, color="black")
plt.plot(x,med, color='blue')
plt.plot(x,mMin, color='blue', linestyle='--')
plt.plot(x,mMax, color='blue', linestyle='--')
plt.xlim(0, 20)
plt.ylim(0, 1)
# help(plt.plot)

plt.savefig('Atividade 3.png')