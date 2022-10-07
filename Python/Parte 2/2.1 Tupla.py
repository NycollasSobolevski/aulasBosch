#tupla
# tupla com as 10 pessoas mais ricas do mundo
#top 3 mais ricos 
#o(a) mais rico do mundo 

tupla = ('Jeff bezos', 'Bill Gates','Warren Buffet', 'Bernard Arnault', 'Carlos Slim Helu', 'Amancio Ortega',
           "Larry Ellison", "Mark Zuckerberg", "Michael Bloomberg", 'Larry Page')

print('\nTop 10 mais ricos do mundo:')


for i in tupla: #em 'for __ in' defini-se um loop ate todos os casos de pessoas, um por um, 'i' é uma variavel 
    print(i)
    #tudo que estiver dentro de 'for  in" será executado em loop ate todos os casos ser executados
    
print('\nTop 3\n',tupla[:3])
print('\nA mais rica:\n',tupla[:1])

