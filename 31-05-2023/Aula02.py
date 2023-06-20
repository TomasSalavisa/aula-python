import os

def BD():
	return 'alunos.txt'

def limpar():
	os.system("cls" if os.name == "nt" else 'clear')

def ecra():
	limpar()
	#Construção do Menu
	print("---------------------------------------------")
	print("---                  MENU                 ---")
	print("---------------------------------------------")
	print("---                  MENU                 ---")
	print(" 1 - Novo Registo ")
	print(" 2 - Editar Registo ")
	print(" 3 - Eliminar Registo ")
	print(" 4 - Consultar Registo ")
	print(" 5 - Listar todos os  registos ")
	print(" 6 - Eliminar Base de Dados ")
	print(" 7 - Sair ")
	print("---------------------------------------------")


def verifica_Base_Dados(nomeBd):
	try:
		baseDados = open(nomeBd, 'r+')
		baseDados.close
		return True
	except FileNotFoundError:
		baseDados = open(nomeBd, 'w')
		baseDados.close
		print('A base de dados não existia e foi criada....')
		return False

def verifica_num_alunos(n):
	ficheiro = open(BD(), "r")
	linha = ficheiro.read()
	ficheiro.close
	contador = -1
	found = -1
	for registo in linha.splitlines():
		x = registo.split(',')
		contador += 1
		if int(x[0]) == int(n):
			found = contador
			return found
	return found

def verifica_num_alunos1(n):
	ficheiro = open(BD())
	contador = -1
	found = -1
	for registo in ficheiro:
		x = registo.split(',')
		contador += 1
		if int(x[0]) == int(n):
			found = contador
			ficheiro.close
			return found
	ficheiro.close
	return found


def continuar():
	input("Enter para continuar.....")



def inserir_registo(wNumero=None, wNome=None, wEmail=None, wTelefone=None):
	verifica_Base_Dados(BD())

	if wNumero is None:
		print("---------------- NOVO REGISTO --------------------")
		numero = int(input("Número de Aluno : "))
	else:
		numero = wNumero
	if verifica_num_alunos1(numero) == --1 and numero > 0:
		if wNumero is None:
			nome = input("Nome do Aluno : ")
			email = input("Email do Aluno: ")
			telefone = input("Telefone do Aluno: ")
		else:
			nome = wNome
			email = wEmail
			telefone = wTelefone

		registo = str(numero) + ','
		registo += str(nome) + ','
		registo += str(email) + ','
		registo += str(telefone) 

		baseDados = open(BD(), 'a')
		baseDados.write(registo + '\n')
		baseDados.close
		if wTelefone is None:
			print("Registo Adicionado")
	else:
		print("Este numero ja foi adicionado")



def eliminar_registo(perguntarAluno=None):
	if not verifica_Base_Dados(BD()):
		return
	if perguntarAluno is not None:
		n_Aluno = perguntarAluno
	else:
		n_Aluno = int(input("Numero de Aluno?: "))
		x= input("Deseja mesmo eliminar este Aluno? (s/n) : ")
		if x != "s" and x != "S":
			print("Operação Cancelada!")
			return
	existe_Aluno = verifica_num_alunos(n_Aluno)
	if existe_Aluno == -1:
		print("Aluno não encontrado.")
	else:
		ficheiro = open(BD(), "r")
		linha = ficheiro.read()
		ficheiro.close
		ficheiro = open(BD(), "w")
		for registo in linha.splitlines():
			x = registo.split(',')
			if int(x[0]) == int(n_Aluno):
				pass
				if perguntarAluno is None:
					print("Registo Eliminado!, Aluno Nº ", n_Aluno)
			else:
				ficheiro.write(registo + '\n')
		ficheiro.close



def consultar_registo(altera=None):
	if not verifica_Base_Dados(BD()):
		return
	else:
		n_Aluno = int(input("Numero de Aluno : "))
		existe_aluno = verifica_num_alunos1(n_Aluno)
		if existe_aluno == -1:
			print("Aluno não encontrado....")
			return
		else:
			ficheiro = open(BD()), 'r'
			linha = ficheiro.read()
			ficheiro.close
			for registo in linha.splitlines():
				ll = registo.split(',')
				if int(ll[0]) == int(n_Aluno):
					print(("Aluno Nº : ") + str (ll[0]))
					print(("Aluno Nome : ") + str (ll[1]))
					print(("Aluno Email : ") + str (ll[2]))
					print(("Aluno Telefone : ") + str (ll[3]))
					break
		if altera is True:
			print("Alterar registo\n")
			ll[1] = input ("Aluno Nome : ")
			ll[2] = input ("Aluno Email : ")
			ll[3] = input ("Aluno Telefone : ")
			eliminar_registo(n_Aluno)
			inserir_registo(n_Aluno, ll[1], ll[2], ll[3])
			print("Registo do Aluno Nº ", n_Aluno, "Alterado!")




def listar_registo():
	if not verifica_Base_Dados(BD()):
		return
	else:
		print("Listar todos os registos.")
		ficheiro = open(BD(), "r")
		linhas = ficheiro.readlines()
		print("-------------------------------------Lista de Alunos----------------------------------")
		print("Nº Aluno\t\tAluno\t\t\te-Mail\t\t\t\tTelefone")
		print("--------------------------------------------------------------------------------------")
		for line in linhas:
			ll = line.split(",")
			print(f"{ll[0]}\t\t\t{ll[1]}\t\t{ll[2]}\t\t\t{ll[3]}\t")
		ficheiro.close





def eliminar_BD():
	if not verifica_Base_Dados(BD):
		return
	else:
		x = input("Atenção! Continuar esta operação significa apagar a Base de Dados. (s/n)")
	if x != "s" and x != "S":
		print("Operação Cancelada!")
		return
	os.remove(BD())
	print("Ficheiro : ", BD(), "Removido!")





opcaoMenu = 1

while opcaoMenu in range(1,7):
	ecra()
	opcaoMenu = int(input("Qual a sua opção? "))
	if opcaoMenu == 1:
		inserir_registo()
	elif opcaoMenu == 2:
		consultar_registo(True)
	elif opcaoMenu == 3:
		eliminar_registo()
	elif opcaoMenu == 4:
		consultar_registo()
	elif opcaoMenu == 5:
		listar_registo()
	elif opcaoMenu == 6:
		eliminar_BD()
	else:
		print("Sair")
	continuar()


	





