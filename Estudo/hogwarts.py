def nota_quantitativa(nota):
	if nota in range(19,21):
		return("ELEVADO!")
	elif nota in range(17,19):
		return("MUTO BOM")
	elif nota in range(14,17):
		return("BOM")
	elif nota in range(10,14):
		return("SUFICIENTE")
	elif nota in range (7,10):
		return("INSUFICIENTE")
	elif nota in range(4,7):
		return("MAU")
	elif nota in range (0,4):
		return("MUITO MAU")
	else:
		return("INVALIDA")


for nota in (-1,9.5,7,6,7,13,16.5,18,19,20,31,10):
	print(f'\nNOTA {nota} = {nota_quantitativa(nota)}')

