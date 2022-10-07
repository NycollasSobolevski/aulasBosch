#manipulação de arquivos
# w = write
# a = append
# r = read
#open('nome do arquivo','tipo de execução')


# =============================================================================
#   #Aqui se escreve no arquivo 
# 
# arquivo = open('Arquivo.txt','w')
# 
# arquivo.write('Hello Word\n')
# arquivo.write('Nycollas')
# =============================================================================


# =============================================================================
# 
#   # Aqui se lê o arquivo
# 
# arquivo = open('Arquivo.txt','r')
# print(arquivo.read())
# 
# for i in arquivo:
#     print(i)
#     
# =============================================================================

# with open('arquivo.txt') as arquivo:
    
arquivo = open('Arquivo.txt','r')

cont = arquivo.read()
# print(cont.split(', '))

palavra = input('digite a palavra: ')

cont.strip(', ')
print(cont)
print('Quantas vezes se repete a palavra',cont.count(palavra))


