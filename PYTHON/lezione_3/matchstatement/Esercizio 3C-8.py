frase = input("inserisci una frase (deve terminare con '?' o '!' oppure senza niente.)")


match frase :

    case frase if frase[len(frase)-1]=="?" and len(frase)%2==0:

        print("SI")

    case frase if frase[len(frase)-1]=="?" and len(frase)%2!=0:

        print("NO")

    case frase if frase[len(frase)-1]=="!":
        
        print("WOW")

    case _ :

        print(f"Tu dici {frase}")

    
        



