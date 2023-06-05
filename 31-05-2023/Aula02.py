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


def verifica_BD(nomeBD):
	try:
		baseBados = open(nomeBD, "r+")
		baseBados.close
		return True
	except FileNotFoundError:
		baseBados = open(nomeBD, "w+")
		baseBados.close
		print("Base de Dados não existia e foi criada....")
		return False

def verifica_num_alunos(n):
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
	verifica_BD(BD())

	if wNumero is None:
		print("---------------- NOVO REGISTO --------------------")
		numero = int(input("Número de Aluno : "))
	else:
		numero = wNumero
	if verifica_num_alunos(numero) == --1 and numero > 0:
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
	if not verifica_BD(BD()):
		return
	if perguntarAluno is not None:
		n_Aluno = perguntarAluno
	else:
		n_Aluno = int(input("Numero de Aluno: "))
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
					print("Registo Eliminado!, Aluno Nº ", perguntarAluno)
			else:
				ficheiro.write(registo + '\n')
		ficheiro.close

def consultar_registo(altera=None):
	if not verifica_BD(BD()):
		return
	else:
		n_Aluno = int(input("Numero de Aluno : "))
		existe_aluno = verifica_num_alunos(n_Aluno)
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
			inserir_registo(n_Aluno), ll[1], ll[2], ll[3]
			print("Registo do Aluno Nº ", n_Aluno, "Alterado!")



def eliminar_BD():
	if not verifica_BD(BD):
		return
	x = input("Atenção! Continuar esta operação significa apagar a Base de Dados. (s/n)")
	if x != "s" and x != "S":
		print("Operação Cancelada!")
		return
	os.remove(BD())
	print("Ficheiro : ", BD(), "Removido!")


eliminar_BD()
	





