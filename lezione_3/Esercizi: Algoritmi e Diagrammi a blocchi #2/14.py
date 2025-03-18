punteggio = 0 

while punteggio < 100 : 

    

    dado1 = int(input("inserisci il numero del dado che uscirà : "))
    dado2 = int(input("inserisci il numero del secondo dado che uscirà : "))

    if 1 <= dado1 <= 6 and 1 <= dado2 <= 6 :

        somma = dado1 + dado2

        if dado1 % 2 == 0 and dado2 % 2 == 0  and  somma > 8 :

            punteggio = 100 

        elif dado1 == 6 or dado2 == 6 or somma == 7 : 

            punteggio += 10
        
        else :

            punteggio = 0

            print("sconfitta")
            break

if punteggio >= 100 :

    print("Vittoria")



