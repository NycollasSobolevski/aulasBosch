# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:15:07 2022

@author: disrct
"""

import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("data/respiradores.csv")



########################## grafico de barras #################################


# x=df.MES
# altura=df.TOTAL
# plt.bar(x,altura, 1.5,align= "center", edgecolor="black", )   
# plt.title("COMPRA DE RESPIRADORES POR MÊS")                  
# plt.xticks(rotation = '90')
# plt.yticks(rotation = '45')
# plt.show()
# help(plt.bar)           #help mostra as funções que pode ser usada



# ########################### Soma todas as colunas #############################


# total_por_estado = df.sum()[1:-1]       
# print(total_por_estado)




# x=df.columns[1:-1]
# plt.bar(x, total_por_estado, color = 'black', zorder=3)         #'zorder' organiza a camada do grafico, ou o exixo "Z"
# plt.title('COMPRA DE RESPIRADORES POR ESTADO')
# plt.xticks(rotation='vertical')
# plt.grid(zorder=0)                                          #gera linha de vizualização
# plt.show()


# ########################### Grafico na horizontaal #############################


# plt.barh(df.MES,df.TOTAL, color = 'purple')
# plt.title('COMPRA DE RESPIRADORES POR MÊS')
# plt.show()


# ############################## Grafico de linha ################################


# plt.plot(df.MES,df.PARANA)
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')            #estilo da linha 'dashed' que seria pontilhada
# plt.title("COMPRA DE RESPIRADORES POR MÊS NO PARANÁ")
# plt.show()

# plt.plot(df.MES,df.PARANA, color = 'purple', marker='x', linewidth = 3, markersize=10) # com marcador 'x'
# plt.xticks(rotation='45')
# plt.title("COMPRA DE RESPIRADORES POR MÊS NO PARANÁ")
# plt.grid(linestyle='dashed')
# plt.show()

# help(plt.plot)  # funlçoes que podem ser usada



# ########################### Plot com mais linhas  #############################


# plt.plot(df.MES,df.PARANA,marker='o', label = 'Paraná')         #'label' é o titulo da linha 
# plt.plot(df.MES,df['SÃO PAULO'],marker='o', label = 'São Paulo')
# plt.plot(df.MES,df['SANTA CATARINA'],marker='o', label = 'Santa Catarina')
# plt.legend()
# plt.title("Grafico de linhas com mais de uma linha")
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')
# plt.show()



# ########################### Grafico de dispersão #############################

# plt.scatter(df['MES'],df['PARANA'], label = 'Paraná')
# plt.scatter(df['MES'],df['SANTA CATARINA'], label = 'Santa Catarina')
# plt.scatter(df['MES'],df['GOIAS'], label = 'Goiás')
# plt.scatter(df['MES'],df['PERNAMBUCO'], label = 'Pernambuco')
# plt.scatter(df['MES'],df['AMAPA'], label = 'Amapá')
# plt.legend() #fontsize=10 / prop={"size":10}
# plt.title("Dispersão")
# plt.xticks(rotation=45)
# plt.show()
# help(plt.legend)



############################# mais de um grafico ###############################

# fig, eixo = plt.subplots(nrows = 2, ncols = 2, figsize = (20,20))
# eixo[0][0].bar(df.MES,df.TOTAL)
# eixo[0][1].bar(df.columns[1:-1],df.sum()[1:-1])
# eixo[1][0].scatter(df['MES'],df['GOIAS'], label = 'Goiás')
# eixo[1][1].plot(df.MES,df.PARANA, color = 'purple', marker='x', linewidth = 3, markersize=10)

# eixo[0][0].set_title("Oi")
# eixo[0][0].set_ylabel("Ola")
# eixo[0][0].tick_params(axis='x',  labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
# eixo[0][1].tick_params(axis='x', labelrotation=90)
# eixo[1][0].tick_params(axis='x', labelrotation=45) # os métodos dos eixos de subplots são diferentes das funções do plot
# eixo[1][1].tick_params(axis='x', labelrotation=90)


############################## grafico de pizza ################################

# estados_sul =df.loc[:['PARANA','SANTA CATARINA','RIO GRANDE DO SUL']]
# print(estados_sul)
# print(estados_sul.sum())


# def valor():
#     x=estados_sul.sum()["PARANA"]
#     y=estados_sul.sum()["SANTA CATARINA"]
#     z=estados_sul.sum()["RIO GRANDE DO SUL "]
#     return x,y,z
# sizes=valor()

# p, tx, autotexts = plt.pie(estados_sul.sum(), labels=estados_sul.columns, 
#         autopct="", shadow=True)
# print(autotexts)
# for i, a in enumerate(autotexts):
#     a.set_text("{}".format(sizes[i]))
    
# plt.pie(estados_sul.sum(), labels = estados_sul.columns, autopct=valor)
# plt.title('COMPRA DE RESPIRADORES NO SUL')
# plt.show()





#duas colunas


# print(df.shape)
# print([a-0.25 for a in range(df.shape[0])])
# print([a+0.25 for a in range(df.shape[0])])
# print(df.PARANA)
    
# plt.bar([i-0.25 for i in range(df.shape[0])],df.PARANA, width = +0.25,
#         label = 'Paraná', align = 'edge')

# plt.bar([a+0.25 for a in range(df.shape[0])],df.TOTAL/30,width = -0.25,
#        label = 'Média brasileira', align = 'edge')
# plt.legend()
# plt.grid(color='lightgray',linestyle='dashed')



#dulo eixo 'x'

fig, eixo = plt.subplots(ncols=1,nrows=1,figsize=(10,5))
eixo.plot(df.MES,df.PARANA,label='Paraná', color='darkblue')

eixo2 = eixo.twinx()
eixo2.plot(df.MES,df.TOTAL/30,color='red')

eixo2.tick_params(axis='y', labelcolor='red')
eixo.tick_params(axis='y', labelcolor='darkblue')

eixo.set_ylabel("Paraná", color='darkblue',fontsize=15)
eixo2.set_ylabel("Média brasileira", color='red',fontsize=15)

eixo.grid(color='lightblue')
eixo2.grid(color='pink')

eixo.set_title('Compra de respiradores PARANÁ X Média brasileira', fontsize= 15)

###salvar como imagem

fig.savefig('grafico_parana.png')




