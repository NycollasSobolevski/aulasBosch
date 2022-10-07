# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 09:30:05 2022

@author: disrct
"""
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data/respiradores.csv')



                            ####DESAFIO####


sul = df.loc[:,['PARANA','SANTA CATARINA','RIO GRANDE DO SUL']].sum(axis=1)
norte = df.loc[:,['ACRE','AMAZONAS','AMAPA','PARA','RONDONIA','RORAIMA','TOCANTINS']].sum(axis=1)
nordeste = df.loc[:,['ALAGOAS','BAHIA','CEARA','MARANHÃO','PIAUI','PERNAMBUCO','PARAIBA','RIO GRANDE DO NORTE','SERGIPE']].sum(axis=1)
sudeste = df.loc[:,['SÃO PAULO','ESPIRITO SANTO','MINAS GERAIS','RIO DE JANEIRO']].sum(axis=1)
centro_oeste = df.loc[:,['GOIAS','MATO GROSSO','MATO GROSSO DO SUL','DISTRITO FEDERAL']].sum(axis=1)
regioes = [sul.sum(),norte.sum(),nordeste.sum(),sudeste.sum(),centro_oeste.sum()]



fig, eixo = plt.subplots(nrows = 1, ncols = 2, figsize = (20,8))
eixo[0].pie(regioes,shadow=True,labels=['sul','norte','nordeste','sudeste','centro_oeste'], autopct='%1.1f%%',)
eixo[0].set_title("TOTAL",fontsize=20)




eixo[1].plot(df.MES,df.TOTAL, label = 'TOTAL', color="black")
eixo[1].plot(df.MES,sul, label = 'sul'),
eixo[1].plot(df.MES,norte, label = 'norte'),
eixo[1].plot(df.MES,nordeste, label = 'nordeste'),
eixo[1].plot(df.MES,sudeste, label = 'sudeste'),
eixo[1].plot(df.MES,centro_oeste, label = 'centro_oeste')
eixo[1].legend()
# eixo[1].xticks(rotation='45')
eixo[1].grid('-')



help(plt.pie)
