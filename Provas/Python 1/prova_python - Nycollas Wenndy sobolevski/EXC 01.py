# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:16:26 2022

@author: DISRCT
"""

a = int(input('insira o lado 1:'))
b = int(input('insira o lado 2:'))
c = int(input('insira o lado 3:'))


if abs(b-c)<a<b+c:
    if abs(a-c)<b<a+c:
        if abs(a-b)<c<a+b:
            if a==b and a==c:
                print('o triangulo é équilátero')
            elif  a ==b or a==c or b==a or b==c:
                print('o triangulo é isósceles')
            elif a!=b and a!=c and b!=c:
                print("o triangulo é escaleno")
else:
    print('o triangulo nao é válido')
