from __future__ import annotations
from mytypes import*

class Coinvolgimento : 

    def __init__(self, impiegato : Impiegato , progetto : Progetto , data_coinvolgimento : date):
        self.impiegato = impiegato
        self.progetto = progetto
        self.data_coinvolgimento = data_coinvolgimento


class Impiegato :
    _nome: str
    ...
    _coinvolgimenti: set[Coinvolgimento] # tutti i link dell'impiegato verso i progetti in cui è coinvolto
    
    def __init__(self , nome : str , cognome : str , nascita : date , stipendio : RealGez):
        self._nome = nome 
        self._cognome = cognome
        self.nascita = nascita
        self.stipendio = stipendio
        self._coinvolgimenti: set[Coinvolgimento] = set()

    def aggiungi_progetto(self, progetto : "Progetto" , data : date):
        coinvolgimento = Coinvolgimento(self, progetto , data)
        self._coinvolgimenti.add(coinvolgimento)
        progetto._coinvolgimenti.add(coinvolgimento)

    def rimuovi_progetto(self, progetto : "Progetto" , data : date):
        coinvolgimento = Coinvolgimento(self, progetto, date.today())
        self._coinvolgimenti.discard(coinvolgimento)
        progetto._coinvolgimenti.discard(coinvolgimento)


class Progetto :
    _nome: str # noto alla nascita
    _coinvolgimenti: set[Coinvolgimento] # certamente non noto alla nascita
    
    def __init__(self , nome : str , budget : RealGez):
        self._nome = nome
        self._budget = budget
        self._coinvolgimenti : set[Coinvolgimento] = set()

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGez:
        return self._budget

    def set_nome(self, nome: str):
        self._nome = nome

    def set_budget(self, budget: RealGez):
        self._budget = budget

    def add_impiegato(self ,impiegato: Impiegato, data : date):
        coinvolgimento = Coinvolgimento(impiegato,self,data)
        impiegato._coinvolgimenti.add(coinvolgimento)
        impiegato._coinvolgimenti.add(coinvolgimento)

    def is_coinvolto(self, impiegato : Impiegato) -> bool:
        return impiegato in self._coinvolgimenti

    def ultimo_impiegato_coinvolto(self):
        if not self._coinvolgimenti:
            return None

        ultimo_impiegato = None
        ultima_data = None
        for impiegato,data in self._coinvolgimenti.items():
            if ultima_data is None  or data > ultima_data:
                ultima_data = data
                ultimo_impiegato = impiegato
                
        return ultimo_impiegato

    def remove_impiegato(self, impiegato : Impiegato):
        coinvolgimento = Coinvolgimento(impiegato, self, date.today())
        self._coinvolgimenti.discard(coinvolgimento)
        impiegato._coinvolgimenti.discard(coinvolgimento)


class Dipartimento : 

    def __init__(self , nome : str , telefono : NumeroTelefono , indirizzo : Indirizzo):
        self.nome = nome
        self.telefono = telefono
        self.indirizzo = indirizzo
