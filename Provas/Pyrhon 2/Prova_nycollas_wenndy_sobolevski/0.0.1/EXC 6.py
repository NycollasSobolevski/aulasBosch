# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:30:40 2022

@author: disrct
"""

import pandas as pd
import matplotlib.pyplot as plt

heroi = pd.read_csv("superheroes.csv").dropna()
# print(heroi)
marvel = heroi[heroi['creator']=='Marvel Comics']
Pmarvel = marvel['strength_score'].mean()
gl = heroi[heroi['creator']=='George Lucas']
pGl = gl['strength_score'].mean()
dc = heroi[heroi['creator']=='DC Comics']
pDc = dc['strength_score'].mean()
lego = heroi[heroi['creator']=='Lego']
pLego = lego['strength_score'].mean()
dhc = heroi[heroi['creator']=='Dark Horse Comics']
pdhc = dhc['strength_score'].mean()


plt.bar('Marvel Comics',Pmarvel,color='black',zorder=3)
plt.bar("George Lucas",pGl,color='black',zorder=3)
plt.bar('DC Comics',pDc,color='black',zorder=3)
plt.bar('Lego',pLego,color='black',zorder=3)
plt.bar('Dark Horse Comics',pdhc,color='black',zorder=3)
plt.axis([-1,5,0,100])
plt.xticks(rotation = '45')

plt.grid(zorder=2)
# plt.bar(help)
################################################################################


imortais = heroi[heroi['has_immortality']==1]
imortais = imortais.sort_values(by='combat_score',ascending=False)
print(imortais[:5])

