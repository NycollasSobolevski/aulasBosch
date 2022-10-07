# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:23:08 2022

@author: DISRCT
"""
import random
numero = random.randint(0,1000)
print(numero)
tentativas = 1
while 1:
    escolha = int(input('Escolha um numero: '))
    if escolha == numero:
        print(f'Parabéns você acertou!! o numero é {numero}')
        print(f'Foram necessárias {tentativas} tentativas.')
        break
    elif escolha == numero-3 or escolha==numero+3:
        print('Quase!')
        tentativas += 1
    elif escolha == numero-2 or escolha==numero+2:
        print('Quase!!')
        tentativas += 1
    elif escolha == numero-1 or escolha==numero+1:
        print('Quase!!!')
        tentativas += 1
    elif escolha < numero-3:
        print('Muito baixo')
        tentativas += 1
    elif escolha > numero+3:
        print('Muito alto')
        tentativas += 1




