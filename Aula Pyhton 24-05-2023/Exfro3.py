
#EXERCICIO PRINT NUMEROS IMPARES DENTRO DOS LIMITES PEDIDOS AO USER

LimiteMin = int(input("Introduza um numero inteiro : "))
LimiteMax = int(input("Introduza um numero inteiro : "))

for n in range(LimiteMin, LimiteMax +1,2):
		if n % 2 != 0:
			print("Numeros Impares: " ,n)


# SOLUÇÃO PROFESSOR

imin = int(input("Minimos : "))
imax = int(input("Maximos : "))
if imin % 2 == 0:
	imin += 1
for i in range(imin, imax +1, 2):
	print(i, " " , end=" ")

	
	