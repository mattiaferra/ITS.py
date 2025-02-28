def show_messages(messaggi):
    
    
    for messaggio in messaggi:
        
        print(messaggio)
        
lista= []
for i in range(3):
    messaggio = input("inserisci il messaggio : ")
    lista.append(messaggio)

print("-----------------------------------------------------------")
    
show_messages(lista)

def send_messages( messaggi ,inviati):
    
    while messaggi:
        messaggio = messaggi.pop()
        inviati.append(messaggio)
        

inviati = []
    
send_messages(lista ,inviati)


print("-----------------------------------------------------------")

print("\nMessaggi inviati : ")
show_messages(inviati)


