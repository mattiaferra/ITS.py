nome = input("inserire il nome : ")
genere = input("Digitare m per maschio e f per femmina : ")

print(f"Nome: {nome}")

match genere:

    case "m":
        print("Genere: Maschio")

    case "f":
        print("Genere: Femmina")

    case _ :
        print(f"Mi dispiace {nome}, non e' possibile procedere con la generazione di un documento di identità!")