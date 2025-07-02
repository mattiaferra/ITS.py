'''PATH : str = "lezione_15/ese.txt"
mode : str = "w"
encoding : str = "utf-8"

file = open(PATH, mode)



print(file)
output : str = file.write("Hello Mattia\n")
print(output)'''

#file.close()


with open("lezione_15/ese.txt", "r") as file:
    print(file.read())



with open("lezione_15/ese.txt", "w") as file:
    print(file.write("Qualcosa"))