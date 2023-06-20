#Exercicio 2

UserTemp = int(input("Insira uma temperatura : "))
FahrenheitParaCelsius = (UserTemp-32)*5/9
# print("A sua temperatura em graus Celsius é : ", UserTemp, " e Convertida em Fahrenheit fica : ", CelsiusParaFahrenheit)
# print("A sua temperatura em Fahrenheit é : ", UserTemp, " e Convertida em Celsius fica : ", FahrenheitParaCelsius)
print(f'A sua temperatura em Fahrenheit : {UserTemp} ºF  --> convertida em Celsius fica {FahrenheitParaCelsius:04.2f} ºC')

#SOLUÇÃO DO PROFESSOR

# farh= float(input("Valor em Fahrenheit : "))
# cen = (farh-32)*5/9
# print(f'{farh}ºF = {cen:08.2f}ºC')