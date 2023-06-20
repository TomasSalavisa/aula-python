#Exercicio 10

# Sexo = str(input("Qual o seu sexo (Homem ou Mulher) : "))
# Altura = float(input("Introduza a sua altura: "))

# if Sexo == "Homem" or "homem": 
# 	PesoIdeal = (72.7 * Altura) - 58
# 	PesoIdealFinal = round(PesoIdeal)
# 	print("O seu peso ideal é : ",PesoIdealFinal)
# elif Sexo == "Mulher" or "mulher":
# 	PesoIdeal = (62.1 * Altura) - 44.7
# 	PesoIdealFinal = round(PesoIdeal)
# 	print("O seu peso ideal é : ",PesoIdealFinal)
# else:
# 	print("Introduza um sexo válido!")


#SOLUÇÃO DO PROFESSOR

alt = float(input("Altura : "))
sexo = str(input("Sexo(m/f) : ")).upper
peso = 72.7*alt-58 if sexo == "M" else 62.1*alt-44.7
ideal = int(peso)
if peso -ideal >= 0.5:
	ideal+1
print(f'Peso Ideal : {ideal}')


