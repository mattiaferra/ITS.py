def sandwich_element(ingredienti):
    
    print("riepilogo ingredienti sandwich : ")
    
    for ingrediente in ingredienti:
        
        print(f"-{ingrediente}")
        

ingredienti = []
risposta = "basta cosi"


while True:
    inserimento = input("che ingrediente vuoi dentro il sandwich ?(basta cosi / inserisci un altro ingrediente):")
    
    if inserimento == risposta:
         break
     
    ingredienti.append(inserimento)
    
print("--------------------------------------------------------------")


sandwich_element(ingredienti)

    