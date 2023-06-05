# Fazer um interaçao com o for, imprimir os elementos da lista com o for
# 

# dog_name = ["Pincher" , "Bulldog Inglês" , "Bulldog Francês" , "RottWeiller"] # -> lista
# dog_name = ["Pincher" , "Bulldog Inglês" , "Bulldog Francês" , "RottWeiller"] # -> set


# procurar por port . e imprimir só por porte.
caes = [{'Raça' : 'Pincher' , 'Port' : 'Pequeno' , 'Classificação' : '***'},
		{'Raça' : 'Bulldog Ingles' , 'Port' : 'Medio' , 'Classificação' : '*'},
		{'Raça' : 'Bulldog Frances' , 'Port' : 'Medio' , 'Classificação' : '**'},
		{'Raça' : 'Rotweiller' , 'Port' : 'Grande' , 'Classificação' : '*****'}]


escolha_caes = input("Escoha um porte (Pequeno/Medio/Grande) :  ").strip()

encontrou=False

for n, dicionario in enumerate(caes):
	if dicionario['Port'] == str(escolha_caes):
		if encontrou == False:encontrou= True
		for campo, conteudo in dicionario.items():
			print(f'Indice : {n}, {campo} : {conteudo}')
		print()

print('Este porte não existe.') if encontrou == False else None
# 

#print da lista com for

# for n in dog_name:
# 		print(n)



# # Agora com indice :

# for n , raca in enumerate(dog_name):
# 		print(f'Indice :  {n}, Raça : {raca}')

	