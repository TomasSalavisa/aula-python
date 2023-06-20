# Exercise 2: Print the sum of the current number and the previous number


# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
print("Printing current and previous number in a range(10)")
previous_num = 0
for n in range(1, 11):
	soma = previous_num + n 
	print("Current Number : ", n, " Previous Number: ", previous_num, " Sum : ", soma)
	previous_num = n