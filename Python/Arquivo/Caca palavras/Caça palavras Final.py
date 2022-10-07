import random

#================================================ VARIÁVEIS =================================================

arquivo = open('palavras.txt','r')
palavras = arquivo.read()
cutword = palavras.split()


a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']




#=========================================== COMEÇO DO JOGO ==============================================

print('''
                                                                  ###
                                                                  ##
  ####     ####     ####     ####             ######    ####      ##      ####    ##  ##   ######    ####     #####
 ##  ##       ##   ##  ##       ##             ##  ##      ##     ##         ##   ##  ##    ##  ##      ##   ##
 ##        #####   ##        #####             ##  ##   #####     ##      #####   ##  ##    ##       #####    #####
 ##  ##   ##  ##   ##  ##   ##  ##             #####   ##  ##     ##     ##  ##    ####     ##      ##  ##        ##
  ####     #####    ####     #####             ##       #####    ####     #####     ##     ####      #####   ######
                     #                        ####

      ''')



while True:
    p =cutword[random.randint(0,len(cutword))]
    d =cutword[random.randint(0,len(cutword))]
    b =cutword[random.randint(0,len(cutword))]
    c =cutword[random.randint(0,len(cutword))]
    
    matriz1=f'''
           O J V F J A F O
           S H G K F A D G 
           S L O B F N S A 
           T P O R G N F S
           F {c[:1]} {c[1:2]} {c[2:3]} {c[3:4]} {c[4:5]} {c[5:]} W
           H A L I G U N A 
           V U T J M D A W
           S I L I T O R Q
           '''
    
    matriz2=f'''
           R A S G V S R Y
           A R F O P {d[:1]} L O
           I R I D O {d[1:2]} C I
           P L O R A {d[2:3]} P U
           I R A S C {d[3:4]} D Q
           L M J H M {d[4:5]} J L
           I U R T A {d[5:]} O U
           '''
           
    matriz3=f'''
           A B C D E R F R
           S {p[:1]} L O L W O R
           Y S {p[1:2]} U Y T R J
           D I L {p[2:3]} H P L W
           G N L D {p[3:4]} J D L
           D A F Y E {p[4:5]} L L
           S D G D G K {p[5:]} W
           '''
    
    
    matriz4=f'''
           A I R I O N {b[5:]} P
           D Q P O R {b[4:5]} J G
           O S L U {b[3:4]} N G E 
           L P L {b[2:3]} I R E A 
           Q O {b[1:2]} D P Y D G
           E {b[:1]} S F Y P T L
           T G J R F C O W
           '''

    
    print('\n\n\n-------- Nível 1 --------\n\n\n',matriz1.upper())

    while True:
        try:
            user = input('digite seu chute: ')
            if user==c:
                print ('\n\n------- Parabéns, proximo nível: --------')
                break
            else:
                print('Tente novamente')
        except:
            print('')
            
    
    print('\n\n\n-------- Nível 2 --------\n\n\n',matriz2.upper())
    
    
    while True:
        try:
            user = input('digite seu chute: ')
            if user==d:
                print ('\n\n------- Parabéns, proximo nível: --------')
                break
            else:
                print('Tente novamente')
        except:
            print('')
            
            
    print('\n\n\n-------- Nível 3 --------\n\n\n',matriz3.upper())
    
    while True:
        try:
            user = input('digite seu chute: ')
            if user==p:
                print ('\n\n------- Parabéns, proximo nível: --------')
                break
            else:
                print('Tente novamente')
        except:
            print('')
            
    print('\n\n\n-------- Nível 4 --------\n\n\n',matriz4.upper())
    
    while True: 
        try:
            user = input('digite seu chute: ')
            if user==b:
                print ('\n\n------- Você concluiu os quatro niveis --------')
                break
            else:
                print('Tente novamente')
        except:
            print('')
            
#=========================================== RESET ==============================================


    print('--------Jogar Novamente?--------- \n \'N\' - Não\n\' S\' - Sim')
    try:
        again = input('Deseja Jogar Novamente? ')
        if again=='n':
            print('---------FIM DE JOGO---------')
            break
        else:
            print('--------JOGAR NOVAMENTE--------')
    except:
        print('Digite \'N\' ou \'S\'')