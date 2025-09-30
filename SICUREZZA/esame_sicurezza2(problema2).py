'''
TRACCIA SECONDO ESERCIZIO

Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata... '''

from Crypto.Util.number import inverse


n = 51151902024533551
e = 3
C = 10002041662569686

# divisori di n

def fattorizza(n):

    for i in range(2, int(n**0.5)+1):

        if n % i == 0:

            return i, n // i
        
    return None, None


p, q = fattorizza(n)


phi = (p - 1) * (q - 1)


d = inverse(e, phi)


m = pow(C, d, n)

#per trasformare il numero decifrato in una stringa

def int_to_ascii(n):
    
    hex_string = hex(n)[2:]

    if len(hex_string) % 2:

        hex_string = '0' + hex_string

    return bytes.fromhex(hex_string).decode('utf-8')

messaggio = int_to_ascii(m)
print("Messaggio decifrato:", messaggio)