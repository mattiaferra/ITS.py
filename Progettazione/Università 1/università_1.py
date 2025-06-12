from mytypes import *




class Facoltà:

    def __init__(self,nome: str, id_facoltà: str ):

        self.nome = nome
        self.id_facoltà = id_facoltà



class Corso:

    def __init__(self, nome:str , id_codice : str , durata_ore: RealGez):
        
        self.nome = nome
        self.id_codice = id_codice
        durata_ore = durata_ore


class Studenti:

    def __init__(self, nome : str  ,codice_fiscale : CodiceFiscale , data_nascita : date, anno_iscr : RealGez , num_matricola :str ):
        
        self.nome = nome 
        self.codice_fiscale = codice_fiscale
        data_nascita = data_nascita
        anno_iscr = anno_iscr
        num_matricola = num_matricola


class Corso_superato_studente:

    def __init__(self,corso : Corso , voto : Voto):
        
        self.corso = corso 
        self.voto = voto


class Professori : 

    def __init__(self , nome : str , data_nascita : date , codice_fiscale : CodiceFiscale):
        
        self.nome = nome
        self.data_nascita = data_nascita
        codice_fiscale = codice_fiscale



class Città:

    def __init__(self, nome: str):
        
        self.nome = nome
        

class Regione:
    def __init__(self, nome: str):

        self.nome = nome
       

        