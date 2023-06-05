greeting = str(input("Greeting : "))


if greeting[0:5] == "hello" or greeting[0:5] == "Hello" :
	print("0$")
elif greeting[0] == "h" and greeting != "hello":
	print("20$")
else:
	print("100$")

