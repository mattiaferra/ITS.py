from PROGETTAZIONE import mytypes
from datetime import *
from abc import ABC



class PostOggetto:
    _prezzo: RealGEZ
    _anni_garanzia: IntGEZ
    _descrizione: str
    _pubblicazione: datetime  # immutable
    _is_nuovo: bool           # immutable
    _condizione: Condizione

    def __init__(self, prezzo: RealGEZ) -> None:
        self._prezzo = self.set_prezzo(prezzo)
        self._anni_garanzia = self.set_anni_garanzia(anni_garanzia)
        self._descrizione = descrizione
        self._is_nuovo = is_nuovo
        self._condizione = condizione 
        self._pubblicazione = datetime.now()

    def set_prezzo(self, p: RealGEZ) -> None:
        # a evoluzione vincolata 
        self._prezzo = p

    def set_anni_garanzia(self, a: IntGEZ) -> None:
        # a evoluzione vincolata 
        self._anni_garanzia = a

    def set_descrizione(self, d: str) -> None:
        # a evoluzione vincolata 
        self._descrizione = d


    def set_condizione(self, c : str)-> None:
        
        condizione = Condizione(c)
