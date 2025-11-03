def cronometro (fun):
    def wrapper(): #inner function / funzione interna
        import time # l' import si può fare tranquillamente anche fuori 
        start = time.time() # time punto time serve per chiedere che ore sono adesso 

        fun() #fun è una funzine generica (astratta) ed è anche un parametro 

        print(time.time() - start) # richiedo che ore sono per calcolare il tempo trascorso

    return wrapper #quando non metto le parentesi ''()'' sto ritornando la zona di memoria in cui wrapper è stata scritta



@cronometro # il @cronometro equivale a scrivere prova = cronometro(prova)

def prova():
    print("ciao")

prova()  # Chiamiamo la funzione decorata per eseguire tutto