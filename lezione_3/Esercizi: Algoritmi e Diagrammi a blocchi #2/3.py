nome_corso = input("Inserisci il nome del corso: ")
max_posti = 100
opzione = input("Scegli un opzione tra: iscrivi, annulla, visualizza, elimina, esci: ")

while True:

    match opzione:

        case  "iscrivi":
            if max_posti > 0:
                max_posti -= 1
            else:
                print("Non ci sono posti disponibili")
                break

        case "annulla":
            if max_posti < 100:
                max_posti += 1
            else:
                print("Tutti i posti sono già disponibili")
                break

        case "visualizza":
            print(f"I posti disponibili sono: {max_posti}")
            print(f"I posti occupati sono: {100-max_posti}")
            break

        case "elimina":
            input("Inserisci il nome di un altro corso: ")
            
        case "esci":
            print("Sei fuori dal programma")
            break