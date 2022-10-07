# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:16:03 2022

@author: disrct
"""
lista = []
placar = 6
ponto  =0 

palavra = input("insira uma palavra:\n>")
lista = list(palavra)
acerto = []

print(f"Dica: a palavra tem {len(lista)} letras.\n\n")

try: 
    while placar > 0 and ponto != len(lista):
        print(f"Letras acertadas: {acerto}")
        escolha = input("escolha uma letra:\n>")
        
        if escolha in lista:
            ponto +=1
            print(f"Voce acertou!! \nSeus pontos são {ponto}")
            acerto.append(escolha)
        else:
            placar -=1
            print(f"Você errou.\nVocê tem mais {placar} tentativas")

except:
    print('Letra errada')
    
print('\n\n-------- Acabou o Jogo --------\n\n')



print("Palavra\n",lista)