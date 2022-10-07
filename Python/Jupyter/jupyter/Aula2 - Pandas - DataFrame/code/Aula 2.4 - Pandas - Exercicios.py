# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:48:28 2022

@author: disrct
"""

import pandas as pd



titanic = pd.read_csv("Data/titanic.csv")
titanic.head()



###############################################################################################################
# med = titanic["Age"].mean()
# print(med)

# titanic["Age"] = titanic.Age.fillna(med)    #primeiro fomos na coluna "age" em seguida demos um "fillna" (troca os valores de "nan" por alguma coisa, que seria "med")

# print(titanic.Age)


################################################################################################################


# pessoas_por_cabine = titanic.groupby("Cabin").count()
# pessoas_por_cabine.head()
# print(pessoas_por_cabine["PassengerId"])
# # print (titanic)



# fem = titanic[titanic["Sex"]=="female"]
# agrFem 

idade_por_sexo = titanic.groupby("Sex")["Age"].mean()
ihomem = idade_por_sexo["male"].mean()
print("homem",ihomem)
imulher = idade_por_sexo["female"].mean()
print("mulher",imulher)


mulher = titanic[titanic["Sex"]=="female"]
mulher["Age"] = mulher.Age.fillna(imulher)