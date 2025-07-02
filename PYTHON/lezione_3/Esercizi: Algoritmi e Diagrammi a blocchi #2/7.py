cont = 0
somma = 0

scelta = input("inserisci la scelta (SI | NO) : ").upper()
        

if scelta == "SI" :

    while True :

        voto : int = int(input("inserisci un voto : "))
        

        if voto > 0 :

            scelta = input("vuoi continuare a inserire voti (SI | NO) : ").upper()
            cont = cont + 1
            somma = somma + voto

        else :

            print("Errore il voto deve essere positivo")
            

        if scelta == "NO" :

            break

while True:

    if cont > 0 :
             
        media = somma/cont
        print("\n------------------------------------")
        print(f"media = {media}")
        break

    else :
    
     print("nessun voto inserito")


            

        
         
