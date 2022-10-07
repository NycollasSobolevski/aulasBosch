#função principal

def verifica(p1,prova):
    dentro=0
    fora=0
    
    for i in range(len(p1)):    
        if i == len(p1)-1:
            x2 = p1[0][0]
            y2 = p1[0][1]
        else:
            x2 = p1[i+1][0]
            y2 = p1[i+1][1]

        x1 = p1[i][0]
        y1 = p1[i][1]
        xp = prova[0]
        yp = prova[1]
        u = [(y2 - y1),(x2 - x1)]
        v = [(y1 - yp),(x1 - xp)]
        f = (u[0]*v[1]) - (u[1]*v[0])

        if f > 0:
            dentro +=1
        elif f < 0 :
            fora += 1
        
    if fora == 0:
        return 1
    if fora >= 1:
        return 0

#Variáveis: 
pol = [(10,10),(5,8),(3,5),(5,0),(11,1),(14,6)] # Nosso polígono
t1 = [(5,5),(15,10)]                            # Nossos pontos


escolha = int(input(f"Escolha qual voce quer testar: \n{t1}:\n>"))
res = verifica(pol, t1[escolha-1])
if res == 1:
    print("Está dentro")
elif res == 0:
    print("Está fora")
