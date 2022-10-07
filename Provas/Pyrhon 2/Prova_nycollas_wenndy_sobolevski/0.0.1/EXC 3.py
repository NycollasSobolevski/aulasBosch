# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:32:20 2022

@author: disrct
"""

def frases(num,):
    lista = []
    invert = []
    palindromo =[]
    listaSemEspaço = []
    for i in range(num):
        frase = input(f"insira a {i+1}° frase: ")
        lista.append(frase)
        listaSemEspaço.append(frase.replace(" ",""))
        
        length_str=len(frase)
        sliced_str=frase[length_str::-1] 
        invert.append(sliced_str.replace(" ", ""))
        print (sliced_str)
        # if lista[i] == invert[i] and listaSemEspaço[i]:
        #     palindromo.append(lista[i])
    # print(lista)
    # print(invert)
    # print(palindromo)
    for i in range(len(lista)):
        if invert[i] == listaSemEspaço[i]:
            palindromo.append(lista[i])
    

    print("\n\nSão palindromos:\n")
    for i in palindromo:
            print(i)
    
    
escolha = int(input("Insira um numero: "))
frases(escolha)