from enum import *
from typing import Any, Self
import re
from datetime import *



class Genere(StrEnum):
    uomo=auto()
    donna=auto()


class CodiceFiscale:
    def __init__(self, codice):
        controllo=bool(re.fullmatch(r"^[A-Z]{6}\d{2}[A-Z]{1}\d{2}[A-Z]\d{3}[A-Z]", codice))
        if controllo==False:
            raise ValueError("Codice fiscale non corretto")
        self.codice=codice
    
    def __hash__(self) -> int:
        return hash(self.codice)


class Valuta(str):
    def __new__(self, valuta: str|Self) -> Self:
        controllo=bool(re.fullmatch(r"^[A-Z]{3}", valuta))
        if controllo==False:
            raise ValueError("Valuta fiscale non corretto")
        self.valuta=valuta


class Denaro:
    # tipo composto dai seguenti campi:
    # - importo: Reale (float)
    # - valuta: Valuta

    _importo: float
    _valuta: Valuta

    def __init__(self, importo: float, valuta: Valuta) -> None:
        self.importo=importo
        self.valuta=valuta

    def importo(self) -> float:
        return self._importo

    def valuta(self)->Valuta:
        return self._valuta
    
    def __hash__(self):
        return hash((self.importo(), self.valuta()))
    
    def __eq__(self, other: Self) -> bool:
        if hash(self) != hash(other):
            return False
        return self.valuta()==other.valuta() and self.importo()==other.importo()
    
    def __add__(self, other: Self) -> Self:
        if self.valuta()!=other.valuta():
            raise ValueError("Le valute sono idverse")
        somma: float=self.importo() + other.importo()
        return Denaro(somma, self.valuta()) # resituisce una nuova istanza di Denaro
    
    def __repr__(self) -> str:
        match self.valuta():
            case 'EUR':
                val="€"
            case 'USD':
                val="$"
            case 'GBP':
                val="£"
            case _:
                val=self.valuta()
        return f"{self.importo()} {val}"


class Città:
    def __init__(self, nomeC):
        self.nomeC=nomeC
    def __hash__(self) -> int:
        return hash((self.nomeC))
    
    def __eq__(self, other: Self) -> Self:
        if hash(self)!=hash(other):
            return False
        return self.nomeC == other.nomeC


class Regione: 
    def __init__(self, nomeR):
        self.nomeR=nomeR
    def __hash__(self) -> int:
        return hash((self.nomeR))
    def __eq__(self, other: Self) -> Self:
        if hash(self)!=hash(other):
            return False
        return self.nomeR == other.nomeR


class Nazione: 
    def __init__(self, nomeN):
        self.nomeN=nomeN
    def __hash__(self) -> int:
        return hash((self.nomeN))
    def __eq__(self, other: Self) -> Self:
        if hash(self)!=hash(other):
            return False
        return self.nomeN == other.nomeN
    
class CAP (str):
    def __new__(cls, v: str | Self) ->Self:
        if re.fullmatch(r"^\d{5}$",v):
            return super().__new__(cls,v)
        raise ValueError(f"'{v}' non è un CAP italiano valido!")


        
class Indirizzo:
    _via:str
    _civico:str
    _cap:CAP
    def __init__(self, via:str, civ:str, cap:CAP) ->None:
        if not via or via.isdigit()==True:
            raise TypeError("La via non può essere vuota e non può contenere solo numeri")
        elif len(civ)>6:
            raise ValueError("Civico inesistente")
        self._via=via
        self._civico=civ
        self._cap:CAP=cap
    
    def via(self) -> str:
        return self._via
    
    def civico(self) -> str:
        return self._civico
    
    def cap(self) ->str:
        return self._cap


class Voto(int):
    def __new__(cls, v:int|float|Self) -> Self:
        if v<18 or v>30:
            raise ValueError("Il voto deve essere compreso tra 18 e 30")
        return int.__new__(cls, v)


class Studente:
    def __init__(self, matricolaS: str, nome: str, genere:Genere, indirizzo: Indirizzo, codicefiscale:str, anno_iscrizione:int):
        self.matricolaS=matricolaS
        self.nome=nome
        self.genere=genere
        self.indirizzo=indirizzo
        self.codicefiscale=codicefiscale
        self.anno_iscrizione= anno_iscrizione

    def __hash__(self) -> int:
        return hash(self.matricolaS)
    

class Posizione(StrEnum):
    ricercatore=auto()
    profAssociato=auto()
    profOrdinario=auto()


class Professore:
    def __init__(self, cf: CodiceFiscale, nome:str, cognome:str, matricolaP:str, ruolo: Posizione, data_nascita:date):
        self.cf= cf
        self.nome=nome
        self.cognome=cognome
        self.matricolaP=matricolaP
        self.ruolo=ruolo
    
    def __hash__(self) -> int:
        return hash(self.matricolaP)


class PositiveInt(int): # la classe eredita dal tipo 'int'
    # tipo di dato intero > 0
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)  # trasforma l'oggetto n in un oggetto int, super si riferisce alla superclasse di PositiveInt (ovvero int)
        if n>0:
            return n
        raise ValueError(f"Numero inseirto non positivo")

indirizzo1=Indirizzo("Via Mattia Battistini", "52")
indirizzo2=Indirizzo("Via del Forte Boccea", "115")
st=Studente("12234", "pippo", "uomo", indirizzo1, CodiceFiscale("VLNDRD03S28H501I"))
st1=Studente("2234", "pina", "donna", indirizzo2, CodiceFiscale("VLNDRD03S28H501I"))

if hash(st)==hash(st1):
    raise ValueError("Due studenti non possono avere stesso numero di matricola")



class NumeroTelefono(str):
    n:str

    def __new__(cls, n:str):
        if n != re.compile(r"^(?:\+39\s?)?(?:(?:3\d{2})|(0\d{1,3}))[\s.-]?\d{6,7}$"):
            raise ValueError("rispettare i parametri per il numero di telefono")
        return str.__new__(n)
    
class RealeMaggioreDiZero:
    def _init_(self, reale):
        if reale > 0:
            self.reale = reale
        else:
            raise ValueError(f"Il numero {self.reale} è minore di zero")

    def _str_(self):
        return f"Il numero scelto è {self}"
    

class RealGez(float):
    def __new__(cls,v:int | float | str | bool |Self) -> Self:
        n:float =super().__new__(cls, v)

        if n>=0:
            return n
        raise ValueError(f"Il numero inserito {v} è negativo")

class PositivaInt1900(int):
    def __new__(cls, valore: int|float|str|bool|Self) -> Self:
        n:int = super().__new__(cls, valore)  # trasforma l'oggetto n in un oggetto int, super si riferisce alla superclasse di PositiveInt (ovvero int)
        if n>1900:
            return n
        raise ValueError(f"Numero inseirto non e' maggiore di 1900")