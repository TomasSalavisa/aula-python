# 1 - Faça um programa em Python que assuma duas variáveis, uma “a=10”, outra “b=20”. Depois da atribuição troque o conteúdo das variáveis.

a= 10
b= 20

a,b=b,a

print("a=",a)
print("b=",b)

# 2 - Faça um programa em Python que assuma um valor adequado para a temperatura de uma cidade em graus Fahrenheit. Escreva um programa para converter essa temperatura em graus centígrados e imprima ambas as temperaturas.

tempF = 110
tempC = 30
FahrToCelsius = (tempF-32)*5/9
CelsiusToFahr = (tempC/5)*9+32
print(f'A sua temperatura de Fahrenheit para Celsius fica {FahrToCelsius} e de Celsius para Fahrenheit fica {CelsiusToFahr}')

# 3 - Converta o valor float 4.33 para String.

print(str(4.33))

# 4 - Arredondar o número 45.8382 à segunda casa decimal.

num = 45.8382
r=round(num,2)
print(r)

# 5 -  Resolva (passo a passo, apresentando os cálculos de como chegar ao resultado final) as seguintes expressões matemáticas:
# A) 3 ** 6 // 8 % 2
# B) 10 ** 2 // 9 – 2
# C) 20 + 3 – 2 % 3 + 9 - 4
# D) 9 / 10 + 10 - 56 * 8 // 3 

A = 3**6//8%2
print(f'A) {A}')
B = 10**2//9-2
print(f'B) {B}')
C = 20+3-2%3+9-4
print(f'C) {C}')
D = 9/10+10-56*8//3
print(f'D) {D}')

# 6 - De entrada dos 3 lados de um triangulo em cm, e informe através de uma mensagem se o triangulo é válido ou não. Um triangulo é válido sse a soma de dois lados for maior que o maior dos 3 lados

num1 = float(input('Give me a number: '))
num2 = float(input('Give me another number: '))
num3 = float(input('Give me another number: '))

if num1 + num2 > num3 or num1 + num3 > num2 and num2 + num3 > num1:
	print("The triangule is valid!")
else:
	print("the triangule is invalid!")

# 7 - Uma cadeia de lojas está a fazer uma promoção em que oferece um desconto de 11% se o valor de compras for superior ou igual a 100 euros. Construa um Programa em Python que leia o valor de compras e de seguida imprima o valor a pagar

preco = int(input('Whats the price of your shooping: '))
if preco >= 100:
	precofinal = preco * 0.9
	print(f'The final price is {precofinal} €')
else:
	print(f'The price is {preco} €') 

# 8 - Escreva um programa em pyton que solicite ao utilizador um número inteiro e de seguida imprima o seu nome em inglês se estiver entre um e cinco ou "Unknow" caso contrário

num = int(input("Digite um número inteiro entre 1 e 5: "))
list = ['One','Two','Three','Four','Five']
if num ==1:
	print(num, "in English is", list[0])
elif num == 2:
	print(num, "in English is", list[1])
elif num == 3:
	print(num, "in English is", list[2])
elif num == 4:
	print(num, "in English is", list[3])
elif num == 5:
	print(num, "in English is", list[4])
else:
	print("Unknown")

# 9 - Construa um programa em python que permita ordenar 3 números reais introduzidos pelo utilizador de forma decrescente.

num1 = float(input('Enter a number : '))
num2 = float(input('Enter a number : '))
num3 = float(input('Enter a number : '))
list = [num1,num2,num3]
list.sort(reverse=True)
print(list)

# 10 - Tendo como entrada a altura e o sexo de uma pessoa, construa um programa em python que calcule seu peso ideal, utilizando as seguintes Fórmulas:
# para homens: (72.7 * Altura) – 58
# para mulheres: (62.1 * Altura) – 44.7
# O programa deve imprimir o inteiro mais próximo do peso ideal.

altura =float(input('Enter your altura em metros: '))
sexo = str(input('Enter your genero M/F: '))

if sexo == 'M' or 'm':
	pesoideal=(72.7*altura)-58
	print(f'Your ideal peso é: {pesoideal} kilos')
elif sexo == 'F' or 'f':
	pesoideal=(62.1*altura)-44.7
	print(f'Your ideal peso é: {pesoideal} kilos')
else:
	print('Please enter a real gender')

