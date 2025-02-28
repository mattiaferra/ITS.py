def show_messages(messaggi):
    
    
    for messaggio in messaggi:
        
        print(messaggio)
        
lista= []
for i in range(3):
    messaggio = input("inserisci il messaggio : ")
    lista.append(messaggio)

print("-----------------------------------------------------------")
    
show_messages(lista)
