# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:49:42 2022

@author: disrct
"""

import pandas as pd


boston = pd.read_csv("Data/BostonHousing.csv", sep=",")     #'sep' de separador

#pegando somente as colunas 'crim' e 'medv' nas primeiras 14 linhas 

print(boston.loc[:13,["crim","medv"]])     #fomra 1 

 

print(boston[['crim','medv']].head(14))     #forma 2


