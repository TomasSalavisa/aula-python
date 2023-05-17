def CalcularNota() :
	 
	nota = int(input("Introduza a sua nota : "))
	
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
	CalcularNota()
	



	



