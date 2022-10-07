import math


#================================================== exercicio 1 ============================================

# class Casa():
#     def __init__(self, Area, Cor, Rua, Nome=None):
#         self.Area = Area
#         self.Cor = Cor
#         self.Rua = Rua
#         self.Nome = Nome
#     def mostre(self):
#         print(self.Area)
#         print(self.Cor)
#         print(self.Rua)
#         print(self.Nome)
#         # print({})



# casa = Casa("140","azul","presidente Faria","João")

# casa.mostre()




#================================================== exercicio 2 ============================================
# class Carro():
#     def __init__(self,marca,modelo,ano,motor):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.motor = motor
#         Carro.gasolina = True
        
        
    

#     def mostra(self):
#         if Carro.gasolina == True:
#             gas = "com"
#         else:
#             gas="sem"
#         print(f'{self.marca} {self.modelo}, {self.ano} com motor de {self.motor}cv e {gas} gasolina')
        
        
#     @staticmethod
#     def Gasolina():         #torna 'Gasolina' true ou false para todos os objetos dessa classe
#         Carro.gasolina = False
#         print('nem todos carros tem gasolina ')
        
        
# carro2 = Carro('chevrolet','cruze','2015','200',)
    

    
# carro1 = Carro('Honda','Civic','2002','120')

# Carro.Gasolina()

# carro1.mostra()
# carro2.mostra()



#================================================== exercicio 2 ============================================

class Calculadora():
    def soma(self,numero1,numero2):
        resultado = numero1+numero2
        print(resultado)
    def sub(self,numero1,numero2):
        resultado = numero1-numero2
        print(resultado)
    def div(self,numero1,numero2):
        resultado = numero1/numero2
        print(resultado)
    def mult(self,numero1,numero2):
        resultado = numero1*numero2
        print(resultado)
        
class Cientifica(Calculadora):
    
    def raiz(self,valor1):
        print(f'{math.sqrt(valor1)}')
    def quad(self,valor1):
        print(f'{math.pow(valor1, 2)}')
        
        
calculadora1 = Cientifica()
calculadora1.soma(5,5)
        











