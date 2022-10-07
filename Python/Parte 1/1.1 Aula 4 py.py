print("\nExemplo 1\n")

s = "n y c o ll a.s"
print('usando s.split(\' \')')
print(s.split(" "))     #usando Split que separa os 
print('usando s.split(\'.\')')
print(s.split("."))






print('\nExemplo 2\n')

Empresa = 'Robert','Bosch','Curitiba'
print('usando \'_\'.join()')
print('_'.join(Empresa))






print("\nExemplo 3\n")

#fatiamento de strings
nome = 'Nycollas Wenndy Sobolevski'
print('Fatiando strings usando \'[0:0]\'')
print(nome[0:])    #vai do caracter '0' da variavel 'nome' ate o final porque nao tem numero determinado pra terminar
print(nome[:8])     # vai do começo da variavel ate o oitavo caracter 





print('\nExemplo 4\n')

#transformar tudo em maiusculo(.upper) ou minusculo(.lower)
print('Transformando texto em maiusculo ou minusculo')
print(nome.upper()) #funcao .upper() transforma o texto em maiusculo
print(nome.lower()) #funcao .lower() transforma o texto em minusculo 




print('\n\nExercicio 2')
print('Pegando as 3 primeiras letras do nome e deixando em maiuscula')
nome = input('Nome: ')
print(nome[:3].upper())





print('\n\nExercicio 3')

nomeCompleto = input('Nome Completo: ')
print(nomeCompleto.title())
print(len(nomeCompleto.replace(' ','')))


