# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:17:36 2022

@author: DISRCT
"""

import numpy as np

notas = open('data/notas.txt','w')
notas.write('nome, nota1, nota2, nota3, média\n\n')


while 1:
    print('''cadastro e consulta
          1 - cadastrar
          2 - consultar
          3 - sair
          ''')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        notas = open('data/notas.txt','a')
        nome = input('Insira o nome do aluno: ')
        n1 = float(input('Insira a nota 1: '))
        n2 = float(input('Insira a nota 2: '))
        n3 = float(input('Insira a nota 3: '))
        media = []
        media.append(n1)
        media.append(n2)
        media.append(n3)
        media = float(np.mean(media))
        # print ('media',media)
        print('\n\n\n')
        media = str(media)
        
        notas.write(nome)
        notas.write(f', {media}\n')
                    
                    
    elif escolha == 2:
        # consulta = input('Nome: ')        
        notas = open('data/notas.txt','r')
        print(notas.read())       
    elif escolha == 3:
        break
        
    


