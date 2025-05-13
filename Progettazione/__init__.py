from Progettazione import mytypes

print("__name__ all'interno di studente : " + __name__)

class Studente:

    matricola : int
    nome : str
    genere : Genere.mytypes


# Importiamo tutto dal modulo 'enum' della libreria standard di Python.
# Questo modulo serve a definire enumerazioni (insieme di valori costanti).
from enum import *

# Definiamo una enumerazione chiamata 'Genere' che estende StrEnum.
# 'StrEnum' è una classe speciale introdotta in Python 3.11 che unisce il comportamento
# delle stringhe (str) e delle enum, permettendo di trattare i valori come stringhe.

class Genere(StrEnum):
    uomo = auto()   # 'auto()' assegna automaticamente il valore 'uomo' come stringa
    donna = auto()  # assegna automaticamente il valore 'donna' come stringa
    

"""Con StrEnum, i membri dell'enumerazione sono trattati sia come oggetti Enum, sia come stringhe.
Quindi puoi usare metodi come .upper() o .lower() direttamente su Genere.uomo, cosa che non potresti fare con una normale Enum."""

# Questo blocco si esegue solo se il file viene eseguito direttamente (non importato come modulo).
if __name__ == "__main__":

    # Stampa il valore associato all'enum Genere.uomo
    print(Genere.uomo)  # Output: Genere.uomo (ma siccome è uno StrEnum, stampa 'uomo')

    # Stampa il tipo dell'oggetto Genere.uomo
    print(type(Genere.uomo))  # Output: <enum 'Genere'> (ma è anche una str)

    # Stampa il valore dell'enum donna in maiuscolo, grazie al fatto che è una stringa
    print(Genere.donna.upper())  # Output: 'DONNA'

    # Stampa il tipo dell'oggetto Genere.donna
    print(type(Genere.donna))  # Anche qui: <enum 'Genere'>

"""StrEnum è molto utile perché:

    Ti permette di limitare i valori ammessi (solo uomo o donna).

    È leggibile e sicuro, evitando errori di battitura come "donnaa" che non verrebbero rilevati con una semplice stringa.

    È compatibile con stringhe, quindi puoi fare operazioni di confronto e manipolazione stringa (come .upper(), .lower(), ecc)."""