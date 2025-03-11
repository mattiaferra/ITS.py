x = int(input("Inserisci x : "))

if x > 0:

    sum = 0 


    for i in range(10):  

        n = int(input("Inserisci un numero : "))

        if x % 2 == 0:  

            if n > x / 2:  

                sum += n

        elif x % 2 != 0:  

            if n < x:  

                sum += n

    print("La somma finale è:", sum)


else:
    
    print("Errore, x deve essere positivo.")
