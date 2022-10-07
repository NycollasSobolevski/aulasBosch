# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:53:59 2022

@author: DISRCT
"""

import pandas as pd 
import matplotlib.pyplot as plt





titanic = pd.read_csv("data/titanic.csv")


fig, eixo = plt.subplots(nrows = 2, ncols=2, figsize=(20,15))


mortos = titanic[titanic['Survived']==0]
mortos = len(mortos)
vivos = titanic[titanic['Survived']==1]
vivos = len(vivos)

eixo[0][0].figsize=(10,10)
eixo[0][0].bar('Survived',vivos, color='pink',edgecolor='black')
eixo[0][0].bar('Not Survived',mortos, color='pink',edgecolor='black',)
eixo[0][0].set_title('Quantidade de vivos e mortos')
eixo[0][0].tick_params(axis='x',  labelrotation=90)



##############################################################################

# # import pandas as pd
# # import matplotlib.pyplot as plt

df = pd.read_csv('data/titanic.csv')

df['Relatives'] = df["SibSp"] + df['Parch']


def count_parentes(registros):
    return registros["Relatives"].count()
parentes = df.groupby('Relatives').apply(count_parentes)
parentes = parentes.reset_index()

def count_irmaos(registros):
    return registros["SibSp"].count()

irmaos = df.groupby("SibSp").apply(count_irmaos)
irmaos = irmaos.reset_index()

def count_filhos(registros):
    return registros["Parch"].count()

filhos = df.groupby("Parch").apply(count_filhos)
filhos = filhos.reset_index()
eixo[0][1].figsize=(10,10)
eixo[0][1].plot(parentes['Relatives'], parentes[0], marker = 'o', label = 'Total de Parentes')
eixo[0][1].plot(irmaos['SibSp'], irmaos[0], marker = 'x', color='orange', label='Número de irmão/cônjuges a bordo')
eixo[0][1].plot(filhos['Parch'], filhos[0], marker = 'v',color = 'green', label='Número de filhos/pais a bordo')

eixo[0][1].legend()
eixo[0][1].grid(True)
eixo[0][1].set_xticks([0,1,2,3,4,5,6,7,8,9,10])
eixo[0][1].set_xlabel('Quantidade de parentes')
eixo[0][1].set_ylabel('Quantidade de pessoas')

# ##############################################################################



homem = titanic[titanic['Sex']=='male']
mulher = titanic[titanic['Sex']=='female']

hIdade = homem.Age.value_counts()
mIdade = mulher.Age.value_counts()

hIdade = hIdade.reset_index()
mIdade = mIdade.reset_index()
eixo[1][0].figsize=(10,10)
eixo[1][0].scatter(hIdade['index'], hIdade['Age'], color='b')
eixo[1][0].scatter(mIdade['index'], mIdade['Age'], color='orange')
eixo[1][0].set_ylabel('Quantidade de pessoas')
eixo[1][0].set_xlabel('Idade')
