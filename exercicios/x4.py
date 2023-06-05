#Exercicio das bolas do bingo com for

from random import randint
bolas=[]
for n in range(1,91):
	bolas.append(n)
while len(bolas) > 0:
	x = randint(1,90)
	while (x in bolas):
		print(bolas.pop(bolas.index(x)),'',end='')
print("\nTerminado")

