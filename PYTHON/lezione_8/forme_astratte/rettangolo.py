from forma_generica import FormaGenerica

class Rettangolo(FormaGenerica):
    
    # inizializzare un oggetto della classe Rettangolo
    def __init__(self):
        super().__init__()

        self.setShape("rettangolo")

    def draw(self) -> None:
        print(f"\n{self.getShape()}\n")

        # outer for , il ciclo for piu esterno
        for i in range(5):

            # inner for , cilco for interno al for
            for j in range(5*2):

                # lato a e lato b del rettangolo
                if i == 0 or i == 5 -1:
                    print("*", end=" ") # di defult python va a capo  e cio serve ad avere come ultimo carattere uno spazio

                # lato c e lato b del rettangolo
                elif j == 0 or j == (5*2) - 1:
                    print("*", end=" ")

                #stampare spazi bianchi 
                else:
                    print(" ", end=" ")

            print("\n", end="")
