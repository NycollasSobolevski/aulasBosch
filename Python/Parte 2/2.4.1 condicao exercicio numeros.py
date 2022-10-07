#loop 'while'
#crie um programa para somar todos os numeros até a escolha do usuario(limite)

escolha = int(input('escolha seu numero: '))
inicio = 0
resultado = 0

while escolha!=inicio:
        inicio+=1   #quando for adicionar mais um valor usa-se '+="
        print(inicio)
        resultado+=inicio
    
print('end')
print('total =',resultado)