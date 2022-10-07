# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:34:08 2022

@author: DISRCT
"""



# def crip(senha):
#     alfabeto={'a':'0000','b':'0001','c':'0010','d':'0011','e':'0100','f':'0101','g':'0110','h':'0111','i':'1000','j':'1001',
#               'k':'0001_0000','l':'0001_0001','m':'0001_0010','n':'0001_0011','o':'0001_0100','p':'0001_0101','q':'0001_0110','r':'0001_0111','s':'0001_1000',
#               't':'0001_1001','u':'0010_0000','v':'0010_0001','w':'0010_0010','x':'0010_0011','y':'0010_0100','z':'0010_0101',
#               '0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001',
#               }
#     code = []
#     senha = list(senha)
#     for i in senha:
#         l = alfabeto[i]
#         code.append(l)
#     code = '_'.join(code)
#     print(code)
    
    



# senha = input('Insira a senha a ser codificada: ')
# crip(senha)


############################################################################

# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto = [chr(i)for i in range(97,123)]

# numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numero = [int(x) for x in range(10)]

print(numero)
print(alfabeto)
Balfabeto = []
Balfabeto = []


def Password(password):
    novaSenha = ""
    for char in password:
        if char.isalnum() == False:
            novaSenha += "0"
        elif char in alfabeto:
            novaSenha += str(alfabeto.index(char.lower()))
        else:
            novaSenha += str(char)
    return novaSenha
            

def passwordToBin(string):
    novaSenha = ""
    senha = Password(string)
    for i in senha:
        novaSenha += format(int(i),"b").zfill(4) + "_"         # 'b' de binario em format, zfill preenche 
    return novaSenha[:-1]


senha = input("> ")
print(Password(senha))
print(passwordToBin(senha))
