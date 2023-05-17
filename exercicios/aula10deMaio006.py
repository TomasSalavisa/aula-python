import sys

def eUmNumero(numero) : 

	try:
		val = int(numero)
		return True
	except ValueError:
		try:
			val = float(numero)
			return True
		except ValueError:
			return False

def Calcular_Produto (fator1, fator2) :
	return fator1 * fator2

def ajuda_utilizador():
	print('Sao necessarios dois argumentos' + \
		   ', sintaxe : ' + sys.argv[0] + ' Arg1 Arg2')


if __name__ == '__main__' :
	if len (sys.argv) < 3:
		ajuda_utilizador()
		sys.exit(1)
		print('ESte print nunca vai acontecer')
elif not eUmNumero(sys.argv[1] or not eUmNumero(sys.argv[2])):
	print('Todos os argumentos devem ser numericos')
	sys.exit(1)
else:
	ft1=float(sys.argv[1])
	ft2=float(sys.argv[2])
	produto= Calcular_Produto(ft1,ft2)
	print(ft1, 'x' , ft2, '=', produto)
