import sys

def Calcular_Produto(fator1, fator2) :
	return fator1 * fator2


if __name__ == '__main__' : # o pyhton deixa usar o len(), porque é uma função builtin.
	if len(sys.argv) < 3:
		print("Sao necessarios 2 argumentos" + \
			   ", sintaxe : " + sys.argv[0] + "Arg1 Arg2")
	ft1 = int(sys.argv[1])
	ft2 = int(sys.argv[2])
	produto = Calcular_Produto(ft1,ft2)
	print(f'{ft1} x {ft2} = {produto}')


# python .\aula10deMaio005.py 60 60
