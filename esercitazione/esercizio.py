'''def countdown(n : int):

    if n < 0 :

        print("Error!" "Inserted number is negative!")

    
    elif n == 0 :

        print(0)

    else :

        print(n)
        countdown(n-1)






countdown(0)
countdown(-5)
countdown(5)'''


#esercizio Scrivi una funzione chiamata sum che prende come input un numero intero positivo n e restituisce la somma dei numeri da 0 a n.
#Se il numero di input n è negativo, visualizza un messaggio di errore e la funzione deve restituire None.
#Per implementare la funzione sum, devi utilizzare esclusivamente un ciclo while e il parametro n passato come input alla funzione.
#È consentito dichiarare solo una variabile all'interno della funzione per gestire la somma.
#Poi, chiama la funzione sum per n = -5 e n = 5.


''''
def somma(n:int):

    if n < 0 :

        print("Error! Inserted number is negative!")
        return None

    else :

        somma = 0

        while n >= 0 :

            somma = somma + n 
            n -= 1
            
            
        return int(somma)



riultato1 = somma(-5)
riultato2 = somma(5)


print(riultato1)
print(riultato2)'''



#Scrivi una funzione sumInRange che calcola la somma di tutti gli interi tra a e b, inclusi, dove a e b vengono passati come input alla funzione.

#Per risolvere l'esercizio, è obbligatorio usare un ciclo while e si assume che il valore di b sia sempre maggiore del valore di a. Pertanto, se a > b, è necessario scambiare i valori per garantire che a sia il più piccolo dei due.

#Infine, è consentito dichiarare solo una variabile, oltre ai parametri della funzione, per memorizzare la somma.

#Poi, chiama la funzione sumInRange per a = 5, b = 10 e per a = 10, b = 5.


'''def sumInRange(a:int ,b:int):

    somma = 0

    if b < a :

        a ,b = b ,a

        
    while a <= b :

        somma += a
        a += 1 

    print(somma)
    return int(somma)


risultato1 = sumInRange(5,10)
print("-------")
risultato2 = sumInRange(10,5)'''

''''

def sumInRange(a: int, b: int):
    
    if a > b:

        return 0
   
    return a + sumInRange(a + 1, b)


risultato1 = sumInRange(5, 10)
print(risultato1)

print("-------")

risultato2 = sumInRange(10, 5)
print(risultato2)'''


