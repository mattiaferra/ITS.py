from typing import List, Optional

class Nazione:
    def __init__(self, nome: str):
        self.nome = nome
        self.citta: List['Citta'] = []

class Citta:
    def __init__(self, nome: str, abitanti: int, nazione: Nazione):
        assert abitanti >= 0, "Gli abitanti devono essere >= 0"
        self.nome = nome
        self.abitanti = abitanti
        self.nazione = nazione
        nazione.citta.append(self)

class Compagnia:
    def __init__(self, nome: str, anno: int, sede: 'Citta'):
        assert anno > 1900, "L'anno deve essere > 1900"
        self.nome = nome
        self.anno = anno
        self.sede = sede

class Aeroporto:
    def __init__(self, codice: str, nome: str, citta: 'Citta'):
        self.codice = codice
        self.nome = nome
        self.citta = citta

class Volo:
    def __init__(self, codice: str, durata_min: int, compagnia: Compagnia,
                 partenza: Aeroporto, arrivo: Aeroporto):
        assert durata_min > 0, "La durata deve essere maggiore di 0"
        self.codice = codice
        self.durata_min = durata_min
        self.compagnia = compagnia
        self.partenza = partenza
        self.arrivo = arrivo

