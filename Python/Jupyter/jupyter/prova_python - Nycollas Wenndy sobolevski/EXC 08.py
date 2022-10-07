# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:58:21 2022

@author: DISRCT
"""

import pandas as pd
import matplotlib.pyplot as plt

##############  LER ARQUIVO  ###############

netflix = pd.read_csv('data/netflix_titles.csv')


netflix.info()
netflix = netflix.dropna()      #TIRANDO CALORES 'NAN'


##############  CODIGO  #############

# filmes = netflix[netflix['type']=='Movie']
# americanos = filmes[filmes['country']=='United States']
# estreia = americanos[americanos['release_year']>=2015]
# estreia = estreia[estreia['release_year']<=2020]
# filmes_totais = len(estreia) 
# f15 = estreia[estreia['release_year']==2015].count()
# f16 = estreia[estreia['release_year']==2016].count()
# f17 = estreia[estreia['release_year']==2017].count()
# f18 = estreia[estreia['release_year']==2018].count()
# f19 = estreia[estreia['release_year']==2019].count()
# f20 = estreia[estreia['release_year']==2020].count()

# plt.bar('2015',f15,zorder=2, color='black')
# plt.bar('2016',f16,zorder=2,color='black')
# plt.bar('2017',f17,zorder=3,color='black')
# plt.bar('2018',f18,zorder=4,color='black')
# plt.bar('2019',f19,zorder=5,color='black')
# plt.bar('2020',f20,zorder=6,color='black')
# plt.grid(zorder=0)
# plt.title('Filmes amricanos 2015 - 2020')


# #######  DURAÇÂO  #######


# brasileiros = netflix[netflix['country']=='Brazil']
# filmesBR = brasileiros[brasileiros['type']=='Movie']
# filmesBR['duration']  = filmesBR['duration'].str.replace('min','')
# filmesBR['duration'] = filmesBR['duration'].sort_values()





############################################################################## 
############################################################################## 
##############################################################################



########## CORREÇÃO ########## 

netflix.info()



americanos = netflix.loc[(netflix['type']== "Movie") &
                         (netflix['country']=='United States') &
                         (netflix.release_year <= 2020) &
                         (netflix.release_year >=2015)]


y = americanos.release_year.value_counts()
x = y.index

plt.bar(x,y, color='black',zorder=2)
plt.title("Filmes americanos 2015 - 2020")
plt.grid(zorder=1,linestyle='dotted')
plt.show()



####### DURAÇÃO ######


def converterToInt(line):
    return int(line[:line.index("m")])

filmesBr = netflix.loc[(netflix['type']=="Movie") &
                       (netflix['country']=='Brazil')]

filmesBr['duration'] = filmesBr.duration.apply(converterToInt)
maisLongos = filmesBr.sort_values(by=['duration'],ascending=False)
maisLongos = maisLongos[:5]

# maisLongos = filmesBr.nlargest(5, "duration", keep="all")

print('Top 5 mais longos: \n',maisLongos)