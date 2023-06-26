# def escreverNome():
# 	name = input("Whats your name: ")
# 	age = input('Whats your age: ')
# 	sex = input('Whats your gender: ')
# 	with open('names.txt', 'a') as file:
# 		file.write(f'------------Profile-------------\nName: {name}\nAge: {age} \nGender: {sex}\n')

# def imprimirNome():
# 	with open('names.txt', 'r') as file:
# 		for line in file:
# 			print(line)

# def eliminarNomes():
# 	with open('names.txt', 'w') as file:
# 		print("'Registos apagados")

# def Menu():
# 	print('---------------------------------------------------Lista de Nomes----------------------------------------------------------')
# 	print('1 - Inserir Novo Nome')
# 	print('2 - Imprimir Nomes da lista')
# 	print('3 - Eliminar Nomes da lista')


# Opcao = 1
# while Opcao in range(1,4):
# 	Menu()
# 	Opcao = int(input('Qual a sua opção: '))
# 	if Opcao == 1:
# 		escreverNome()
# 	elif Opcao == 2:
# 		imprimirNome()
# 	elif Opcao == 3:
# 		eliminarNomes()
# 	else:
# 		print("Sair")
# 	print()
# 	print('Enter para continuar...')


dic = [{"Nome" : "Joao", "Idade": "21", "Sexo": "Macho"},
	   {"Nome" : "Tomas", "Idade": "45", "Sexo": "Macho"},
	   {"Nome" : "Miguel", "Idade": "81", "Sexo": "Gigachad"},
	   {"Nome" : "Maria", "Idade": "17", "Sexo": "Female"},]
for i in dic:
	print(f'\nNome: {i["Nome"]} \nIdade: {i["Idade"]} \nSexo: {i["Sexo"]}')
	
