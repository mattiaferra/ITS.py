voto = int(input("inserisci il voto da assegnare : "))

match voto:

    case 1|2|3:
        print("Gravemente Insufficente")

    case 4|5:
        print("Insufficente")
    
    case 6|7:
        print("Sufficente")
    
    case 8|9:
        print("Molto Buono")

    case 10:
        print("Eccellente")
    
    case _ :
        print("Voto non valido")