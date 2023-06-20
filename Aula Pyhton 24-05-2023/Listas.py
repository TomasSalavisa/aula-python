def conversor_nota(nota):
	if  19 <= nota <= 20:
		return"Elevado"
	elif 17 <=  nota <= 19:
		return"Muito Bom"
	elif 14 <=  nota <= 17 :
		return"Bom"
	elif 10 <=  nota <= 14 :
		return"Suficiente"
	elif 7 <=  nota <= 10 :
		return"Insuficiente"
	elif 3 <=  nota <= 7 :
		return"Mau"
	elif  0 <= nota <= 3 :
		return"Muito Mau"
	else:
		return("Insira uma nota valida")

if __name__ == "__main__":
	for nota in (-1,0.1,0,3,9,5,17,20,15):
		print(f'{nota}\t: {conversor_nota(nota)}')