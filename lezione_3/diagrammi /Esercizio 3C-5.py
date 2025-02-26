profilo = {}

profilo["nome"] = input("inserisci un nome : ")

profilo["ruolo"] = input("inserisci il ruolo : ")

profilo["eta"] = int(input("inserisci età : "))


match (profilo["ruolo"], profilo["eta"]):

    case ("admin", _):

        print("Accesso completo a tutte le funzionalità.")

    case ("moderatore", _):

        print("Può gestire i contenuti ma non modificare le impostazioni.")

    case ("utente",eta) if eta < 18 :

        print("Accesso limitato! Alcune funzionalità sono limitate!")

    case ("utente", _):

        print("Accesso completo alle funzionalità standard.")

    case ("ospite", _):

        print("Accesso ristretto! Solo visualizzazione dei contenuti.")

    case _:

        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")




