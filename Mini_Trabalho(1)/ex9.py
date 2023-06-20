#Exercicio 9

Num1 = int(input("Introduza um numero : "))
Num2 = int(input("Introduza um numero : "))
Num3 = int(input("Introduza um numero : "))

Resultado = [Num1,Num2,Num3]
Resultado.sort(reverse=True)
print("Os numeros introduzidos ordenados de forma descrescente : ",Resultado)


#SOLUÇÃO DO PROFESSOR

numeros=[Num1,Num2,Num3]
numeros.sort(reverse=True)
print(f'{numeros[0]}\t{numeros[1]}\t{numeros[2]}\t')

# SOLUÇÃO DO PROFESSOR (Não é a opcional, só para saber como é que o sort() funciona)

# print("Ordernar Números")
# a = int(input("Introduza um numero : "))
# b = int(input("Introduza um numero : "))
# c = int(input("Introduza um numero : "))

# if a<b:
# 	if b<c:
# 		print(f'{b}\t{c}\t{a}')
# 	else:
# 		print(f'{b}\t{a}\t{c}')
# else:
# 	if b<c:
# 		if a<c:
# 			print(f'{c}\t{a}\t{b}')
# 		else:
# 			print(f'{a}\t{c}\t{b}')
# 	else:
# 		print(f'{a}\t{b}\t{c}')
