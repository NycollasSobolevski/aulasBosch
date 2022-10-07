# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:34:39 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("Data/titanic.csv", sep=",")
a = titanic.columns[:-1]

print(titanic.iloc[:,:-1])   #em '[:,:-1]' antes da virgula decidimos o tanto de linhas e depois da virgla o tanto de colunas
print(titanic.loc[:5,["Name","Survived"]])  #aqui queremos todas as linhas da coluna 'Survived' e podemos adicionar mais colunas

#################################################################################################################################


a = titanic.describe()      #mostra dados estatísticos 
print(a)


a = titanic.Age.describe()      #dados estatísticos somente da coluna 'Age'
print(a)


a = titanic.describe().loc[:,["Age","Pclass"]]      #dados estatíscos nas colunas 'Age' e 'pclass'
print(a)


#################################################################################################################################



print('\n\n')


#valores unicos 


print(titanic['Embarked'].unique())


#quantas vezes se repetem


print(titanic['Embarked'].value_counts())


# excluir todas as linhas com not a number 

print(titanic.dropna()) #sempre que uma linha que tem "nan" em alguma celula ele apaga a linha inteira 


#preencher todas as linhas que contem "nan" com alguma coisa 


print(titanic.fillna)
# preencher o "NAN" de alguma coluna especifica
idade = titanic["Age"].fillna('x')      #aonde tem 'nan' será preenchido com 'x'
titanic["Age"] = idade                  #criando uma nova variavel com a coluna 'Age'
print(idade)



#################################################################################################################################


#ele agrupa os elementos ta tabela


# print(titanic.groupby('Embarked').mean()['Age'])


#filtrar


# titanic = titanic.sort_values(by="Age",ascending=True)           #ele ordena os valores pela coluna 'Age'
# print(titanic)


########################################################################################################################
 #filtro 
 # fazer um filtro por sexo e aplicá-lo!
filtro_apenas_mulheres = titanic["Sex"] != "male"
mulheres_titanic = titanic[filtro_apenas_mulheres]
mulheres_titanic["Age"].describe()
print()