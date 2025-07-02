somma = 0
cont = 1

while True:

    n = int(input("inserisci un numero : "))

    if n > 0:

        somma = somma + n
        
    cont+=1

    if cont == 5 :
        break

print(somma)