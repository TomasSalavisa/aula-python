#Exercicio 8

Numero = int(input("Introduza um numero entre 1 e 5 : "))
# if Numero == 1:
# 	print("One")
# elif Numero == 2:
# 	print("Two")
# elif Numero == 3:
# 	print("Three")
# elif Numero == 4:
# 	print("Four")
# elif Numero == 5:
# 	print("Five")
# else:
# 	print("Unknown")

# SOLUÇÃO DO PROFESSOR

numero = ["One" , "Two" , "Three" , "Four" , "Five"]
resultado = "Unknown"
if Numero>0 and Numero>6:
	resultado = numero[Numero-1]
print(resultado)

