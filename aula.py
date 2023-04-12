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


# alunos = ['Jose','Maria','Daniela']
# print('Daniela' in alunos)#false
# print('Maria' in alunos)#true
# print('maria' in alunos)#false
# print('Maria' not in alunos)#false
# print('maria' not in alunos)#true
#output True se estiver na lista, False se nao estiver na lista ou se nao estiver escrito como deve ser ex:'maria' em vez de 'Maria

# x=40
# y=x
# z=40

# print(z)
# print(y)
# print(x is y)


# alunos1 = alunos
# alunos2 = ['Jose','Maria','Daniela']

# print(alunos is alunos1)
# print(alunos is alunos2)

#alunos e alunos2 sao entidades diff, por isso nunca podem ser iguais neste caso True.
#alunos e alunos 1 sao true, pk estao os dois a ocupar so 1 espaço, enquanto alunos esta a ocupar mais do que 1 espaço.

#no jupiter depois ->> dir(__builtin__)
#importar biblioteca 'math' no jupiter --> import(math)

# y="20.3"
# z=20.3
# print(type(y))

# y=float(y)

# print(y)
x='100'
y='20.3'
z=50
w=43.3
m=61.3
t=True


print(x,';' ,y,';',z,';',w,';',m,';',t,';')
print(type(y))
print(type(z))
print(type(w))
print(type(m))
print(type(t))

print(type((10,2)))