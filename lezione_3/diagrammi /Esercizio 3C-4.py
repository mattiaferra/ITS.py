
nome_animale = str(input("inserisci il nome di un animale:"))


Mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli =  ["aquila", "pappagallo", "gufo", "falco"]
Pesci = ["squalo", "trota", "salmone", "carpa"]


match nome_animale:

    case nome_animale if nome_animale in Mammiferi:
        
        print(f"l'animale {nome_animale} appartiene alla categoria dei Mammiferi ")

    case nome_animale if nome_animale in Rettili:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Rettili")

    case nome_animale if nome_animale in Uccelli:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Uccelli")

    case nome_animale if nome_animale in Pesci:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Pesci")

    case _ :

       print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")