# x=1
# y=--1
# z=+-1
# w=0

# print(x,y,z,w) 
# # Print nas 4 variaveis
# print(+x)
# print(not x)
#------------------------------------------------------------------------------------
#operador ternario

# aprovado = True
# print('O aluno ficou ' + ('Reprovado', 'Aprovado')[aprovado])

# #                          OU

# print('o aluno ficou ' + ('Aprovado' if aprovado else ' Reprovado'))

#-------------------------------------------------------------------------------------

# # b="x"
# # c="y"

# print(b,c)
# print(b+c)

#------------------------------------------------------------------------------------------

# alunos = ['Jose','Maria','Daniela']
# print('Daniela' in alunos)#false
# print('Maria' in alunos)#true
# print('maria' in alunos)#false
# print('Maria' not in alunos)#false
# print('maria' not in alunos)#true
#output True se estiver na lista, False se nao estiver na lista ou se nao estiver escrito como deve ser ex:'maria' em vez de 'Maria

#------------------------------------------------------------------------------------------

# x=40
# y=x
# z=40

# print(z)
# print(y)
# print(x is y)

#------------------------------------------------------------------------------------------

# alunos1 = alunos
# alunos2 = ['Jose','Maria','Daniela']

# print(alunos is alunos1)
# print(alunos is alunos2)

#alunos e alunos2 sao entidades diff, por isso nunca podem ser iguais neste caso True.
#alunos e alunos 1 sao true, pk estao os dois a ocupar so 1 espaço, enquanto alunos esta a ocupar mais do que 1 espaço.
#------------------------------------------------------------------------------------------
#no jupiter depois ->> dir(__builtin__)
#importar biblioteca 'math' no jupiter --> import(math)
#------------------------------------------------------------------------------------------
# y="20.3"
# z=20.3
# print(type(y))

# y=float(y)
# print(y)
#-----------------------------------------------------------------------------------------

# x='100'
# y='20.3'
# z=50
# w=43.3
# m=61.3
# t=True


# print(x,';' ,y,';',z,';',w,';',m,';',t,';')
# print(type(x)) string
# print(type(y)) string
# print(type(z)) int
# print(type(w)) float
# print(type(m)) float
# print(type(t)) bool
# print(type((10,2))) tuple -> can hold multiple variables at once

# print(x+y, ';', + z + w)

# #print(x+w)

# print(5*"A") #Escreve a letra 'A' 5x.
# print(500*"A") #Escreve a letra 'A' 500x.

# print(float(80) + float(w))
# print(x+ str(t))

# x=100
# y=10.563
# z=x/y

# print(x.is_integer())
# print(y.is_integer())
# print(z.is_integer())

# x=40
# y=20

# print(x-y)
# print(int.__sub__(x,y))# metodos magicos, codigo so do python para fazer codigo mais facil. 
