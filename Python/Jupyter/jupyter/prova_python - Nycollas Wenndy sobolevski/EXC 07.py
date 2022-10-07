# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:17:36 2022

@author: DISRCT
"""

import numpy as np

notas = open('data/notas.txt','a')


# while 1:
#     print('''cadastro e consulta
#           1 - cadastrar
#           2 - consultar
#           3 - sair
#           ''')
#     escolha = int(input('Escolha: '))
#     if escolha == 1:
#         notas = open('data/notas.txt','a')
#         nome = input('Insira o nome do aluno: ')
#         n1 = float(input('Insira a nota 1: '))
#         n2 = float(input('Insira a nota 2: '))
#         n3 = float(input('Insira a nota 3: '))
#         media = []
#         media.append(n1)
#         media.append(n2)
#         media.append(n3)
#         media = float(np.mean(media))
#         # print ('media',media)
#         print('\n\n\n')
#         media = str(media)
        
#         notas.write(f'{nome}\n{n1}\n{n2}\n{n3}\n{media[:4]}')
#         # notas.write(f', {media[:4]}\n')
                    
                    
#     elif escolha == 2:
#         # consulta = input('Nome: ')        
#         notas = open('data/notas.txt','r')
#         print(notas.read())       
#     elif escolha == 3:
#         break
        
    

#============================================================================


def create():
    data = open('data/notas.txt','a')
    quantA = int(input('quantidade de alunos a cadastrar: '))
    for i in range(quantA):
        notas=[]
        nome = input(f'Aluno {i+1}: ')
        quantNotas = int(input('Quantidade de notas a serem cadastradas: '))
        for j in range(quantNotas):
            nota = float(input(f'Digite a nota {j+1}: '))
            notas.append(nota)
        conteudo = nome + "," + (",".join(str(notas)))
        data.write(conteudo)
    data.close()
         
    
    


def search():
    data = open("data/notas.txt",'r') 
    
    for linha in data:
        a=linha.split(',')
        a[0] == linha 
        print(a[0])
    
    data.close()
    
    aluno = input("Nome do aluno: ")
    
    with open("data/notas.txt","r") as data:
        for linha in data.readlines():
            a = linha.split(",")
            a[1] = a[-1].replace('\n', '')
            if a[0] == aluno:
                a = list(map(float(a[1:])))
                return 
            

        
while 1:        
    print("\n\n1 - Cadastrar aluno \n2 - Consultar")
    opcao = int(input("escolha opção"))
    if opcao==1:
        create()
    if opcao==2:
        print('media do aluno: ', search())
    if opcao ==3:
        break
    
            
        
