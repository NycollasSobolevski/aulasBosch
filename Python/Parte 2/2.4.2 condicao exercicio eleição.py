# =============================================================================
# from datetime import date
# 
# print('\n\n---Eleições---\n')
# 
# nascimento = int(input('Digite ano de nascmineto: '))
# hoje = date.today()
# anoAtual = hoje.year
# idade = anoAtual-nascimento
# print('Você tem',idade,'anos')
# 
# if idade >= 18 and idade<70 :
#         print ('você pode votar!')
# elif idade <18 and idade >= 16:
#         print('voto facutativo')
# elif idade >70:
#     print('voto facutativo')
# else:
#         print('Não pode votar')
#         
# =============================================================================


#loop 'while'
escolha = int(input('escolha seu numero: '))
inicio = 0
resultado = 0

while escolha!=inicio:
        inicio+=1   #quando for adicionar mais um valor usa-se 
        print(inicio)
        resultado+=inicio
    
print('end')
print('total =',resultado)