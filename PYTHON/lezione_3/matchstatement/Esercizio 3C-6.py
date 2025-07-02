
nome_animale = str(input("inserisci il nome di un animale: "))
habitat = str(input("inserisci l' Habitat : (acqua,terra,aria)"))

dizionario_animali = {

    "Mammiferi": ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"],
    "Rettili": ["serpente", "lucertola", "tartaruga", "coccodrillo"],
    "Uccelli": ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"],
    "Pesci": ["squalo", "trota", "salmone", "carpa"]

}

habitat_possibili = {
    
    "Mammiferi": ["terra", "acqua"],
    "Rettili": ["terra", "acqua"],
    "Uccelli": ["aria", "terra"],
    "Pesci": ["acqua"]
}

match nome_animale:

    case nome_animale if nome_animale in dizionario_animali["Mammiferi"]:
        
        print(f"l'animale {nome_animale} appartiene alla categoria dei Mammiferi ")
        animal_type = "Mammiferi"

    case nome_animale if nome_animale in dizionario_animali["Rettili"]:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Rettili")
        animal_type = "Rettili"

    case nome_animale if nome_animale in dizionario_animali["Uccelli"]:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Uccelli")
        animal_type = "Uccelli"

    case nome_animale if nome_animale in dizionario_animali["Pesci"]:

        print(f"l'animale {nome_animale} appartiene alla categoria dei Pesci")
        animal_type = "Pesci"

    case _ :

       print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")
       animal_type = "unknown"


match animal_type:

    case "unknown":
        print("Non sono in grado di fornire informazioni sull'habitat ")

    case _:

        if habitat in habitat_possibili[animal_type]:

            print(f"L'animale {nome_animale} può vivere nell'habitat {habitat}.")

        else:
            
            print(f"L'animale {nome_animale} non può vivere nell'habitat {habitat}.")