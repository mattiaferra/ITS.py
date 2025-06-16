

while True :

    x = int(input("Inserisci X : "))

    if x % 2 == 0 and x > 0 : 
        break

    else:
        print("rinserisci il numero")

lista_sequenze = []

while True :

    numeri = int(input("Inserisci un numero da inserire nella lista : "))
    

    if numeri == 0 :
        break

    elif numeri % 2 == 0 and numeri > 0 : 
        lista_sequenze.append(numeri)

    else:
        print("rinserisci il numero")



print(lista_sequenze)



#cerco x nella lista

contatore = 0

for numero in lista_sequenze:
    if numero == lista_sequenze[numero]:
        

        





