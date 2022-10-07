# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:26:56 2022

@author: disrct
"""

import pandas as pd
titanic = pd.read_csv("Data/titanic.csv")



def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""

    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

def faixa_etaria(linhas):
    idade = linhas["Age"]
    if idade < 12:
        return "criança"
    elif idade >=12 and idade < 18:
        return "adolescente"
    elif idade >=18 and idade < 65:
        return "adulto"
    elif idade >= 65:
        return "idoso"
    else:
        return "nada"
    
    
#################################################### Atividade 01 #####################################################

pessoas = titanic["Survived"].count()
sobreviventes = titanic.Survived[titanic["Survived"]==1]
morte = titanic[titanic["Survived"]==0]
intMortos = titanic.Survived[titanic["Survived"]==0].count()
intVivos = titanic.Survived[titanic["Survived"]==1].count()

# # print (pessoas)
# print ("Total de mortos: ",intMortos)
# print ("Total de Sobreviventes",intVivos)

# # print(calculate_percentage(morte, pessoas)
# # print(calculate_percentage(sobreviventes, pessoas)


# print('\n\nTotal de pessoas no navio')

# primeiraClasse = titanic.Pclass[titanic["Pclass"]==1].count()
# print("\n\nTotal de pessoas da primeira classe: ",primeiraClasse, "\nporcentagem de pessoas da primeira classe: ", calculate_percentage(primeiraClasse, pessoas)) 

# segundaClasse = titanic.Pclass[titanic["Pclass"]==2].count()
# print("\nTotal de pessoas da primeira classe: ",segundaClasse, "\nporcentagem de pessoas da primeira classe: ", calculate_percentage(segundaClasse, pessoas)) 

# terceiraClasse = titanic.Pclass[titanic["Pclass"]==3].count()
# print("\nTotal de pessoas da primeira classe: ",terceiraClasse, "\nporcentagem de pessoas da primeira classe: ", calculate_percentage(terceiraClasse, pessoas)) 
# #---------------------------------------------------------------------------------------------
# print("\n\nMortes: ")

# pclasse = morte.Pclass[titanic["Pclass"]==1].count()
# print('Quantudade de mortos da primeira classe: ',pclasse)
# print("Porcentagem de Mortos da Primeira classe: ",calculate_percentage(pclasse, intMortos))

# sclasse = morte.Pclass[titanic["Pclass"]==2].count()
# print('\nQuantudade de mortos da segunda classe: ',sclasse)
# print("Porcentagem de Mortos da segunda classe: ",calculate_percentage(sclasse, intMortos))

# tclasse = morte.Pclass[titanic["Pclass"]==3].count()
# print('\nQuantudade de mortos da terceira classe: ',tclasse)
# print("Porcentagem de Mortos da terceira classe: ",calculate_percentage(tclasse, intMortos))



#################################################### Atividade 02 #####################################################


# titanic["Faixa_Etaria"] = titanic.apply(faixa_etaria, axis=1)

# Crianças = titanic[titanic["Faixa_Etaria"]=="criança"]
# intCrianças = titanic[titanic["Faixa_Etaria"]=="criança"].count()

# Aultos = titanic[titanic["Faixa_Etaria"]=="adulto"]
# intAultos = titanic[titanic["Faixa_Etaria"]=="adulto"].count()

# Mulheres = titanic[titanic["Sex"]=="female"]

# Idoso = titanic[titanic["Faixa_Etaria"]=="idoso"]
# intIdoso = titanic[titanic["Faixa_Etaria"]=="idoso"].count()

# Adolescente = titanic[titanic["Faixa_Etaria"]=="adolescente"]
# intAdolescente = titanic[titanic["Faixa_Etaria"]=="adolescente"].count()



# mortos_mulheres_crianças = morte.Survived[(titanic["Sex"]== "female")|(titanic["Faixa_Etaria"]=="criança")].count()
# print("Mulheres ou Crianças mortos",mortos_mulheres_crianças)

      
# print("Porcentagem de mulheres ou ciranças mortas: ", calculate_percentage(mortos_mulheres_crianças, intMortos))


#################################################### ############### #####################################################

