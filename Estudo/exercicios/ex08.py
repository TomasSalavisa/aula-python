
# racas_caes = [
# 	{"Raça :" : "Pincher", "Porte: ": "Pequeno" , "Classificação: " : "*****"},
# 	{"Raça :" : "Bulldog", "Porte: ": "Medio" , "Classificação: " : "***"},
# 	{"Raça :" : "Rootweiller", "Porte: ": "Grande" , "Classificação: " : "*"},
# 	]

# for n, dicionario in enumerate(racas_caes):
# 	for campo, conteudo in dicionario.items():
# 			print("Indice : ", n, " " ,campo , "" ,conteudo)

# Demonstrates iterating over a list of dict objects

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print("\nName: ",student["name"],"\nHouse: ",student["house"],"\nPatronus: " ,student["patronus"])

print()