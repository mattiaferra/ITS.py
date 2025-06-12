from mytypes import*


class Impiegato :
    
    def __init__(self , nome : str , cognome : str , nascita : date , stipendio : RealGez):
        
        self.nome = nome 
        self.cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio



class Progetto :
    _nome: str # noto alla nascita
    _impiegati_coinvolti: dict[Impiegato, date] # certamente non noto alla nascita
    
    def __init__(self , nome : str , budget : RealGez):
        
        self._nome = nome
        self._budget = budget
        self._impiegati_coinvolti = dict()



    def get_nome(self) -> str:
         return self._nome

    def get_budget(self) -> RealGez:
        return self._budget

    def set_nome(self, nome: str):
        self._nome = nome

    def set_budget(self, budget: RealGez):
        self._budget = budget


    def add_impiegato(self ,impiegato: Impiegato, data : date):
        self._impiegati_coinvolti[impiegato] = data

        # return self.impiegati_coinvolti
    

    def is_coinvolto(self, impiegato : Impiegato) -> bool:

        return impiegato in self._impiegati_coinvolti
            

    def ultimo_impiegato_coinvolto(self):

        if not self._impiegati_coinvolti:
            return None


        ultimo_impiegato = None
        ultima_data = None


        for impiegato,data in self._impiegati_coinvolti.items():

            if ultima_data is None  or data > ultima_data:
                ultima_data = data
                ultimo_impiegato = impiegato
                
        return ultimo_impiegato
    

    def remove_impiegato(self, impiegato : Impiegato):

        if impiegato in self._impiegati_coinvolti:
              del self._impiegati_coinvolti[impiegato]






            


        




class Dipartimento : 

    def __init__(self , nome : str , telefono : NumeroTelefono , indirizzo : Indirizzo):
        
        self.nome = nome
        self.telefono = telefono
        self.indirizzo = indirizzo
