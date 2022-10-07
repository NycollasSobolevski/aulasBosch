# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:30:44 2022

@author: disrct
"""
import pandas as pd

##################################### ATIVIDADES #####################################


# Uma pessoa quer comprar um carro, e deseja ver as opções mais econômicas. Mostre os dados em um Dataframe com as seguintes condições:
# 
#     Deve ser um carro com 5 lugares; (Passengers)
#     Selecione os 10 carros com maior MPG(Miles Per Gallon) na cidade;
#     Dos 10 mais econômicos, mostre os 5 modelos mais baratos; (Price)
#Mostre somente as colunas 'Manufacturer','Make','Price','MPG.city','Type','Passengers'


# carros = pd.read_csv("Data/Cars93.csv",sep=",")     #abrindo arquivo
# carros = carros.loc[:,["Manufacturer","Make",'Price','MPG.city','Type','Passengers']]  #selecionando as colunas que queremos
# carros = carros.dropna()     # Tirando os veiculos que nao temos todas as informações



# lugares = carros[carros["Passengers"]==5]                                   # selecionando os veículos que tem exatamente 5 passageiros
# economicos = lugares.sort_values(by="MPG.city",ascending=False).head(10)    # colocando o MPG.city em ordem decrescente
# preco = economicos.sort_values(by="Price",ascending=True).head(5)           # Colocando o Price em ordem crescente

# print(preco)
# # print(carros['Passengers'])



########################################################################################################################
# # E se quisermos um filtro que retorne os registros com os passageiros da primeira classe que sobreviveram e os 
# # passageiros da terceira classe que não sobreviveram?


# titanic = pd.read_csv("Data/titanic.csv",sep=',')

# sobreviventes = titanic[titanic["Survived"]==1]
# mortos = titanic[titanic['Survived']==0]
# primeira_classe = sobreviventes[titanic["Pclass"]==1]
# terceira_classe = mortos[titanic["Pclass"]==3]



# print('sobreviventes da primeira classe\n',primeira_classe, '\n\nmortes da terceira classe\n',terceira_classe)

########################################################################################################################

titanic = pd.read_csv("Data/titanic.csv",sep=',')

embarque = titanic[titanic['Embarked']=='S']
classe = embarque[titanic['Pclass']==2]
idade = embarque[titanic['Age']==29.0]
sexo = idade[titanic['Sex']=='female']
nome = sexo[titanic['Name'].str.contains('Anne')]       #'.str.contains' procura uma string dentro do texto

nome = nome.fillna('?')


print(nome)

pessoa = (titanic['Embarked'] =='S') & (titanic['Pclass']==2) & (titanic['Name'].str.contains('Anne')) 















