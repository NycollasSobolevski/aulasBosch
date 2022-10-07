#jogo das palavras
import random 
from random import sample

arquivo = open('palavras.txt','r')
palavras = arquivo.read()
cutWord = palavras.split()
lista = []
selWord = 0
palavra1 = 0
palavraEscolhida = 0
score = int(100)



print('''
      Dificuldade:
      1 - Fácil
      2 - Médio
      3 - Dificil
      ''')



while True:
    while True:
        try:
            dificuldade = int(input('Esclha a dificuldade: '))
            if dificuldade > 0 and dificuldade < 4:
                break
            else:
                print('Digite um NUMERO entre 1 e 3 ')
        except:
            print('')
        
    while True:
        try:
            selScore =int(input('Quantos pontos você quer arriscar? '))
            if selScore >=20 and selScore <100:
                break
            else:
                print('Digite um numero entre 20 e 100')
        except:
            print('')
    

    while True:    
            if dificuldade == 1:
                for i in cutWord[:6]:
                  lista.append(i)
                selWord=random.choice(lista)
                palavra1 = sample(selWord,len(selWord))
                print('\n Adivinhe:\n',''.join(palavra1))
                user = input('Selecione sua palavra: ')
                if user != selWord:
                    score = score-selScore
                    print('Você errou\n','sua pontuação é:',score)
                    break
                if user == selWord:
                    print('Parabéns você acertou!!')
                    break
                
            
            if dificuldade == 2:
                for i in cutWord[6:12]:
                  lista.append(i)
                selWord=random.choice(lista)
                palavra1 = sample(selWord,len(selWord))
                print('\n Adivinhe:\n',''.join(palavra1))
                user = input('Selecione sua palavra: ')
                if user != selWord:
                    score = score-selScore
                    print('Você errou\n','sua pontuação é:',score)
                    break
                if user == selWord:
                    print('Parabéns você acertou!!')
                    break
                
            
            if dificuldade == 3:
                for i in cutWord[12:19]:
                  lista.append(i)
                selWord=random.choice(lista)
                palavra1 = sample(selWord,len(selWord))
                print('\n Adivinhe:\n',''.join(palavra1))
                user = input('Selecione sua palavra: ')
                if user != selWord:
                    score = score-selScore
                    print(f" Você errou!\nSua pontuação é: {score}")
                    break
                if user == selWord:
                    print('Parabéns você acertou!!')
                    break
                    
                
    if score <= 0 :
            print('---------Acabou a pontuação----------')
            break
            
    