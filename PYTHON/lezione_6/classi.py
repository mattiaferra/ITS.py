
class Persona :


    def __init__(self):  #(self ,nome ,eta) non ce bisogno di scriverlo in questo modo perche li chiede in input

        self.nome = input("inserisci nome : ")
        self.eta = input("inserisci eta : ")

    def presentazione(self):

        print(f"Ciao sono {self.nome} e ho {self.eta} anni ")

stampa = Persona()
stampa.presentazione()



