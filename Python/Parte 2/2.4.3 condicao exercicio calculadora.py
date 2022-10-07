#while true
# calculadora
while True:
     
    resultado = 0
    
    primeiro = int(input('Digite o primeiro numero: '))
    print(primeiro)
        
    segundo = int(input('Digite o segundo numero: '))
    print(segundo)
        
    print('''operações:
          1 - soma
          2 - Subtração
          3 - Multiplicação
          4 - Divisão
          5 - Sair''')
          
    operacao =int(input('Digite a operação desejada: '))
    print(operacao)
    
    
    if operacao == 1 :
        print('resultado =',primeiro+segundo)
    if operacao == 2 :
        print('resultado =',primeiro-segundo)
    if operacao == 3:
        print('resultado =',primeiro*segundo)
    if operacao == 4 :
        print('resultado =',primeiro/segundo)
    if operacao == 5 :
        break
    