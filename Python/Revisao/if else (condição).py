# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:11:40 2022

@author: disrct
"""

altura = float(input('insira a altura em cm: '))
peso = float(input('insira o peso em KG: '))

imc = peso/((altura/100)**2)
print(f'Seu IMC é {imc: .2f}')


if imc < 18.5:
    print('Magreza')
if imc > 18.5 and imc <= 24.9:
    print('Seu IMC é Normal')
if imc > 24.9 and imc <= 29.9:
    print('Seu IMC é Sobrepeso com obesidade de grau 1')
if imc > 29.9 and imc <= 39.9:
    print('Seu IMC é Obesidade com obesidade de grau 2')
if imc > 39.9:
    print('Seu IMC é Obesidade GRAVE com obesidade de grau 3')

