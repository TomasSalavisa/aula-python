#Condição de if.... so funciona se estiver no canal main, se nao estiver nao pede o input.

from math import sqrt

a=20

b=30

if __name__ == '__main__':
	a = float(input('Valor para o cateto "a " = ' ))
	b = float(input('Valor para o cateto "b" = '))

c = sqrt(a**2 + b**2)

if __name__ == '__main__':
	print('Para o cateto "a" = ' + str(a) + ' e cateto "20 b " = ' + str(b) + ' e hipotenusa "c" = ' + str(c))




#verificar se 
