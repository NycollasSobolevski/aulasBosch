# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:33:49 2022

@author: disrct
"""
valor = int(input("Insira um valor acima de R$10,00\n> "))

notas100 = (valor-(valor%100))/100
print(f"{notas100} notas de R$100,00")