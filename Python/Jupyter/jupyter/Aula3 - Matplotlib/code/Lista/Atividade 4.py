# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:57:57 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# temperaturas máxima média e mínima média (em graus Celsius)
temp_max = [26.8,	26.8,	26,	24,	20.8,	20.1,	19.7, 21.5,	21.4,	23.1,	25,	26.2]
temp_min = [17.2,	17.4,	16.5,	14.6,	11.2,	9.7, 9, 9.6, 11.1,	13.2,	14.9,	16.2]

fig1,ax1 = plt.subplots(figsize=(10,4))


plt.plot(meses,temp_max, marker='o', color='r', label='Max Temp')
plt.fill_between(meses, temp_max, facecolor='salmon' )
plt.plot(meses,temp_min, marker='o', color='b', label='Min Temp')
plt.fill_between(meses, temp_min, facecolor='cornflowerblue' )
plt.yticks([0,15,30])
plt.axis(xmin = 0,xmax = 11,ymin = 0, ymax = 30)
plt.grid(linestyle='dashed')
plt.ylabel('Temperatura')


plt.xlabel('Meses')
plt.legend()
# help(plt.plot)

plt.savefig('Atividade 4.png')