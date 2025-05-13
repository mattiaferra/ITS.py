from enum import *

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

    print("__name__ all'interno di mytypes.py: " + __name__)




    if __name__ == '__main__':
        
        print(Genere.uomo)
        print(Genere.donna)
