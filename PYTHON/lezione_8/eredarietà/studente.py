# Dal modulo persona.py importo la classe Persona
from lezione_8.eredarietà.persona import Persona

# La classe Studente eredita dalla classe Persona
class Studente(Persona):

    '''
    Attributi della classe Persona in quanto Studente eredita da Persona 
    self.name: str
    self.lastname: str
    self.age: int

    Attributi della classe Studente
    self.matricola: str
    '''

    # Inizializzare un oggetto della classe Studente
    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        super().__init__(name, lastname, age)

        # Istruzioni che inizializzano un oggetto della classe Studente
        self.setMatricola(matricola)

    # Metodi setter

    # Metodo che imposta il valore dell'attributo self.matricola
    def setMatricola(self, matricola: str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("\nErrore! La matricola non può essere rappresentata da una stringa vuota!")

    # Metodo getter

    # Metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self) -> str:
        return self.matricola
    

    # ridefinire il metodo __str__(overiding)

    def __str__(self) -> str:
        return f"\nNome:{self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}"

