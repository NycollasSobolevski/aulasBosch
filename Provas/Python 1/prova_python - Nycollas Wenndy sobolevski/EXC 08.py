# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:58:21 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt

netflix = pd.read_csv('data/netflix_titles.csv')
netflix = netflix.dropna()


filmes = netflix[netflix['type']=='Movie']
americanos = filmes[filmes['country']=='United States']
estreia = americanos[americanos['release_year']>=2015]
estreia = estreia[estreia['release_year']<=2020]
filmes_totais = len(estreia) 
f15 = estreia[estreia['release_year']==2015].count()
f16 = estreia[estreia['release_year']==2016].count()
f17 = estreia[estreia['release_year']==2017].count()
f18 = estreia[estreia['release_year']==2018].count()
f19 = estreia[estreia['release_year']==2019].count()
f20 = estreia[estreia['release_year']==2020].count()

plt.bar('2015',f15)
plt.bar('2016',f16)
plt.bar('2017',f17)
plt.bar('2018',f18)
plt.bar('2019',f19)
plt.bar('2020',f20)


# 