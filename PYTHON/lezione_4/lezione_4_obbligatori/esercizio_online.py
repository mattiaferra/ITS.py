'''def somma_lista():
    
        mylist = [1,2,3,4,5]
        risultato = sum(mylist)
        print(risultato)

somma_lista()'''

'''def somma_liste(lista1 ,lista2):
   

    risultato_1 = sum(lista1)
    risultato_2 = sum(lista2)

    risultato = risultato_1 + risultato_2
    print(risultato)


somma_liste([1,3],[2,2])'''
    

#stringa invertita
'''
def stringa_ivertita():

   stringa = input("inserisci una parola : ")
   print(''.join(reversed(stringa)))

   
  
stringa_ivertita()'''


# funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.

'''
def lista_parole_specificata():

    lista_0 = ["ciao","come","va"]
    lista_1 = ["cocomero","salame","salciccia"]
    lista_specificata = []

    for parola in lista_0:

        if parola[0] == "s":
            lista_specificata.append(parola)

    for parola in lista_1:

        if parola[0] == "s":
            lista_specificata.append(parola)

    print(lista_specificata)


lista_parole_specificata()'''



  # Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.

'''
def num_pari():

    numeri = [1,2,3,4,5]
    numeri_pari = []

    for numero in numeri:

        if numero % 2 == 0:
            numeri_pari.append(numero)
    print(numeri_pari)


num_pari()'''


# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.

'''

def lunghezza_stringa ():
    
    lista = []

    while True:
        
        parola : str = input("inserisci una parola : (invio per terminare)")

        if parola == "":
              break

        lista.append(len(parola))

    print(lista)

lunghezza_stringa()'''  