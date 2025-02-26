
nome_animale = str(input("inserisci il nome di un animale:"))

match nome_animale:

    case "cane"|"gatto"|"cavallo"|"elefante"|"leone":
        
        print(f"l'animale {nome_animale} appartiene alla categoria dei Mammiferi ")

    case "serpente"|"lucertola"|"tartaruga"|"coccodrillo":

        print(f"l'animale {nome_animale} appartiene alla categoria dei Rettili")

    case "aquila"|"pappagallo"|"gufo"|"falco":

        print(f"l'animale {nome_animale} appartiene alla categoria dei Uccelli")

    case "squalo"|"trota"|"salmone"|"carpa":

        print(f"l'animale {nome_animale} appartiene alla categoria dei Pesci")

    case _ :

       print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")