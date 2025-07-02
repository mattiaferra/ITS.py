

max_posti = 27
posti_liberi = max_posti



while True:

    opzioni : str  = input("inserisci una dellle seguenti opzioni : | ingresso | uscita | stato | esci \n")


    match opzioni:

        case "ingresso" if posti_liberi > 0 :

            posti_liberi = posti_liberi - 1

        case"ingresso" :

            print("non ci sono posti ")
            break

        case "uscita" if posti_liberi < max_posti :

            posti_liberi = posti_liberi + 1

        case "uscita" :

            print("tutti i posti sono gia disponibili")
            break

        case "stato" : 

            print(f"posti liberi : {posti_liberi}")
            print(f"posti occupati : {max_posti - posti_liberi}")

        case "esci":

            print("Sei ucito dal parcheggio :) ")
            break

    







