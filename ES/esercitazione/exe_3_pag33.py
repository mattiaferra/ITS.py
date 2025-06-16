'''Esercizio 3 (Cartella 9 ex_3.py)

È data la classe Animal. Per ogni attività, testa le tue modifiche!

1. Crea due istanze realistiche di Animals

2. Stampa il nome di ogni oggetto

3. Modifica la quantità di zampe di un oggetto usando la notazione a punto

4. Aggiungi un metodo setLegs() per impostare le zampe di un oggetto e ripeti l'attività 3 ma
   questa volta usando il metodo.

5. Aggiungi un metodo getLegs() per restituire la quantità di zampe

6. Aggiungi un metodo denominato printInfo che stampa tutti gli attributi di Animal'''





class Animals :

    def __init__(self,type_animal,zampe):

        self.type_animal = type_animal
        self.zampe = zampe

    
    def __str__(self):
        
        return f"{self.type_animal},{self.zampe}"


    def setLegs(self,zampe):

        self.zampe = zampe


    def getLegs(self):

        return self.zampe


    def printInfo(self):

        print(f"Tipo di animale: {self.type_animal}")
        print(f"Numero di zampe: {self.zampe}")

        


cane = Animals("cane","4")
gatto = Animals("gatto","4")

print(cane)
print(gatto)

print("----------------------")

gatto.zampe = 8

print(f"il {gatto.type_animal} ha {gatto.zampe} zampe")




gatto.setLegs(4)

print(gatto)


print(f"con il metodo getLegs il {gatto.type_animal} ha {gatto.getLegs()} zampe.")

print("----------------------")

print("Caratteristiche Animali :\n") 

cane.printInfo()
gatto.printInfo()







        