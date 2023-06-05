file_name = str(input("File name : "))

if ".gif" in file_name:
	print("image/gif")
elif ".jpg" in file_name:
	print("image/jpg")
elif ".jpeg" in file_name:
	print("image/jpeg")
elif ".png" in file_name:
	print("image/png")
elif ".pdf" in file_name:
	print("image/pdf")
elif "txt" in file_name:
	print("image/txt")
elif ".zip" in file_name:
	print("image/zip")
else:
	print("whats that? ")

