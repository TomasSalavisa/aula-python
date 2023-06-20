# Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

number1 = 40
number2 = 30

if number1 * number2 <= 1000:
	print("product: ", number1 * number2)
else:
	print("sum: ", number1+number2)