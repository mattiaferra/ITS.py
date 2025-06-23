import random

class Creatura :

    def __init__(self, nome : str):
        
        self._nome = nome



    def setNome(self,new_name : str):

        if new_name == " ":
            self._nome = "Creatura Generica"

        else:
            self._nome = new_name

    
    def getNome(self):

        return self._nome 
    


    def __str__(self):
        
        return f"Creatura: {self._nome}"
    


class Alieno(Creatura):

    def __init__(self, nome,):

        self.__setMatricola()
        self.__setMunizioni()

        nome = f"Robot-{self._matricola}"

        super().__init__(nome)

        if not self.getNome().startswith("Robot-") or not self.getNome()[6:].isdigit():
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.setNome(nome)

    def __setMatricola(self):

        self._matricola = random.randint(10000,90000)


    def __setMunizioni(self):

        self._munizioni =   [ i ** 2 for i in range(15)]  


    def getMatricola(self):

        return self._matricola


    def getMunizioni(self):

        return self._munizioni       


    def __str__(self):
        return f"Alieno: {self.getNome()}"                                 
    


class Mostro(Creatura):

    def __init__(self, nome , urlo_vittoria : str , gemito_sconfitta : str):
        super().__init__(nome)

        self.nome = nome
        self.urlo_vittoria = urlo_vittoria
        self.gemito_sconfitta = gemito_sconfitta
        self.setAssalto()


    
    def setAssalto(self):
         
        self._assalto = random.sample(range(1, 101), 15)


    def getAssalto(self):

        return self._assalto

      #Da Completare