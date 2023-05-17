#Codigo Meu

def CalcularNota(nota) :
	 
	
	if  19 <= nota <= 20:
		print("Elevado")
	elif 17 <=  nota <= 19:
		print("Muito Bom")
	elif 14 <=  nota <= 17 :
		print("Bom")
	elif 10 <=  nota <= 14 :
		print("Suficiente")
	elif 7 <=  nota <= 10 :
		print("Insuficiente")
	elif 3 <=  nota <= 7 :
		print("Mau")
	elif  0 <= nota <= 3 :
		print("Muito Mau")
	else:
		print("Insira uma nota valida")
	


if __name__ == "__main__" :
	nota = int(input("Introduza a sua nota : "))
	notaFinal = CalcularNota(nota)
	print(CalcularNota(nota))
	

#Codigo do Professor

# def converter_Nota_Quantitativa(nota):
# 	nota = float(nota)
# 	if nota > 20 or nota <0 :
# 		return "Nota Incorreta"
# 	elif nota >= 19 :
# 		return "Elevado"
# 	elif nota >= 17:
# 		return "Muito Bom"
# 	elif nota >= 14:
# 		return "Bom"
# 	elif nota >= 10:
# 		return "Suficiente"
# 	elif nota >= 7:
# 		return "Insuficiente"
# 	elif nota >= 3:
# 		return "Mau"
# 	else:
# 		return "Muito Mau"


# if __name__ == "main":
# 	nota = input("Nota: ")
# 	nota_convertida = converter_Nota_Quantitativa(nota)
# 	print(nota_convertida)

	



