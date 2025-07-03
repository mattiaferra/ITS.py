''' 
Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato lo schema, appena consentitovi dal docente, scrivere una funzione ricorsiva in Python, chiamata printListBackward() che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver che, date le seguenti liste, stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva implementata.

lista1: 1, 2, 3, 4, 5
lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"'''



def printListBackward(lista):
    if not lista:  # Caso base: lista vuota
        return "la lista è vuota"
    print(lista[-1])  # Stampa l'ultimo elemento
    printListBackward(lista[:-1])  # Richiama la funzione con la lista senza l'ultimo elemento

    



lista1 = [1, 2, 3, 4, 5]
lista2 = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

print("Lista 1 al contrario:")
printListBackward(lista1)

print("\nLista 2 al contrario:")
printListBackward(lista2)
