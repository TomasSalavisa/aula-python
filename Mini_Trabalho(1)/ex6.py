#Exercicio 6

lado1 = float(input("Insira um lado do triangulo : "))
lado2 = float(input("Insira um lado do triangulo : "))
lado3 = float(input("Insira um lado do triangulo : "))

if lado1 + lado2 < lado3 : # Esta conta está mal feita 
	print("O triangulo é valido")
else : 
	print("O triangulo não é valido")


#SOLUÇÃO DO PROFESSOR

l1 = int(input("Insira um lado do triangulo : "))
l2 = int(input("Insira um lado do triangulo : "))
l3 = int(input("Insira um lado do triangulo : "))
if l1+l3 <= l3 or l2+l3 <l1 or l1+l3<=l2:
	print("Triangulo Impossivel ")
else:
	print("Triangulo Possivel")