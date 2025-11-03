def cronometro (fun):
    def wrapper(): #inner function / funzione interna
        print("ciao come stai")
        fun() #fun è una funzine generica (astratta) ed è anche un parametro 

    return wrapper #quando non metto le parentesi ''()'' sto ritornando la zona di memoria in cui wrapper è stata scritta



@cronometro # il @cronometro equivale a scrivere prova = cronometro(prova)

def prova():
    print("ciao")

prova()  # Chiamiamo la funzione decorata per eseguire tutto