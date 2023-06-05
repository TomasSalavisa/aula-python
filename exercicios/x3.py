#Exercicio de bolas do bingo com while

from random import randint
bolas = []
y=0
while y < 90:
	y += 1
	bolas.append(y)
while len(bolas) > 0:
	x = randint(1,90)
	while (x in bolas ):
		print(bolas.pop(bolas.index(x)), '',end='')
print("\nTerminado")