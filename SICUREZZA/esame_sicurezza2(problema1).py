'''TRACCIA DEL PRIMO ESERCIZIO 

Sia dato il messaggio cifrato (convertito in numero intero in base 10): 

204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.'''


c = 204751668535
n = 514948966453
e = 3

# Alfabeto: lettere maiuscole e minuscole
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def codifica(parola):
    """Codifica la parola in base 256 come intero"""
    m = 0
    for char in parola:
        m = m * 256 + ord(char)
    return m

# brute force su tutte le combinazioni di 5 lettere
for a in alfabeto:
    for b in alfabeto:
        for d in alfabeto:
            for e_ in alfabeto:
                for f in alfabeto:
                    p = a + b + d + e_ + f
                    m = codifica(p)
                    risultato = pow(m, e, n)
                    
                    if risultato == c:
                        print("La parola è:",p)
