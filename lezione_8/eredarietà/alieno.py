class Alieno:
    '''
    di un alieno ci interessa sapere la galassia di provienienza 
    self.galaxy : str

    '''


    # inizializzare un oggetto della classe alieno
    def __init__(self, galaxy : str):
        self.setGalaxy(galaxy)


    def setGalaxy(self,galaxy : str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore! la galassia di provenienza non può essere vuota")
        


    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print(f"\nfhrhshehghr\n")


    def __str__(self) -> str:
        return f"\n alieno provieniente dalla galassia {self.getGalaxy()}!\n"
    
    
        