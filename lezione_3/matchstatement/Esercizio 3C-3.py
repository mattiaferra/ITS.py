lista = []

for i in range(3):

    cosa = input("inserisci oggetti : m")
    lista.append(cosa)


match lista:
    
    case ["penna", "matita", "quaderno"]:
        print("Materiale Scolastico")
    
    case ["pane", "latte", "uova"] :
        print("Prodotti alimentari")

    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")

    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")

    case _ :
        print("Categoria sconosciuta")