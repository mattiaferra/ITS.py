from film import Film


class Azione (Film):

    def __init__(self, id, title):
        super().__init__(id, title)

        self.__genere = "Azione"
        self.__penale : float = 3 

    def getGenere(self,genere):

        return self.__genere
    
    def getPenale(self,penale):

        return self.__penale
        

    def calcolaPenaleRitardo(self,giorni_ritardo : int):

        calcolo = giorni_ritardo*self.__penale
        return calcolo

    
    class Commedia(Film):

        def __init__(self, id, title):
            super().__init__(id, title)

            self.__genere = "Commedia"
            self.__penale: float = 2.5

        def getGenere(self, genere):

            return self.__genere

        def getPenale(self, penale):

            return self.__penale

        def calcolaPenaleRitardo(self, giorni_ritardo: int):

            calcolo = giorni_ritardo * self.__penale
            return calcolo


class Drama(Film):

    def __init__(self, id, title):
        super().__init__(id, title)

        self.__genere = "Drama"
        self.__penale: float = 2.0

    def getGenere(self, genere):

        return self.__genere

    def getPenale(self, penale):

        return self.__penale

    def calcolaPenaleRitardo(self, giorni_ritardo: int):
        
        calcolo = giorni_ritardo * self.__penale
        return calcolo