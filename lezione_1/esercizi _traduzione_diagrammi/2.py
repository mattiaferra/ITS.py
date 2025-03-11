#primo modo :
'''
massimo = int(input("inserisci un massimo : "))

cont = 1


while cont < 4:

    cont += 1 

    n = int(input("inserisci un numero : "))

    if n > massimo:

        massimo = n

print(massimo)'''


#secondo modo :
'''
massimo = int(input("inserisci un massimo : "))
cont = 1

while True:

    if cont == 4:

        break

    else:
        cont += 1

    n = int(input("inserisci un numero : "))

    if n > massimo:

        massimo = n 

    

print (massimo)'''
       

#Terzo Modo :

massimo = int(input("inserisci un massimo : "))

for i in range(4):

    n = int(input("inserisci un numero : "))

    if n > massimo :

        massimo = n

print(massimo)

