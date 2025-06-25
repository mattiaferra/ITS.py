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

        self.nome = f"Robot-{self._matricola}"

        super().__init__(nome)

        if nome != f"Robot-{self._matricola}":
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")


    def __setMatricola(self):

        self._matricola = random.randint(10000,90000)


    def __setMunizioni(self):

        self._munizioni =   [ i ** 2 for i in range(15)]  


    def getMatricola(self):

        return self._matricola


    def getMunizioni(self):

        return self._munizioni       


    def __str__(self):

        return f"Alieno: {self.getNome()}\n Munizioni : {self._munizioni}"                                 
    


class Mostro(Creatura):

    def __init__(self, nome , urlo_vittoria : str , gemito_sconfitta : str):
        super().__init__(nome)

        self.nome = nome
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)
        self.setAssalto()


    
    def setAssalto(self):
         
        self._assalto = random.sample(range(1, 101), 15)


    def getAssalto(self):

        return self._assalto

      #Da Completar


    def setVittoria(self,vittoria : str):

        if vittoria : 
            self.urlo_vittoria = vittoria
        else:
            self.urlo_vittoria = "GRAAAHHH"


    def setSconfitta(self,sconfitta : str):

        if sconfitta :
            self.gemito_sconfitta = sconfitta
        else:
            self.gemito_sconfitta = "Uuurghhh"
     


    def __str__(self):
        
        nome_mostro = self.getNome()
        nome_char_alternato = ""

        for idx in range(len(nome_mostro)):
            if not idx % 2:
                nome_char_alternato += nome_mostro[idx].upper()
            else:
                nome_char_alternato += nome_mostro[idx].lower()


        return f"Mostro : {nome_char_alternato} \n Assalto : {self._assalto}"

            



def pariUguali(a: list[int], b: list[int]):

    c = []

    for i in range (len(a)) :

        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)

        else:
            c.append(0)

    return c


def combattimento(a:Alieno,m:Mostro):

    if not isinstance(a,Alieno) or not isinstance(m,Mostro):
        print("Errore il combattimento annullato")
        return None
    

    controllo_combattimento = pariUguali(a.getMunizioni(),m.getAssalto())
    cont = 0
    for i in controllo_combattimento:

        if i == 1 :
            cont += 1

    
    if cont >= 4 :
        print((m.urlo_vittoria + "\n") * 3)
        return m
    else:
        print(m.gemito_sconfitta)
        return a
    
    
def proclamaVincitore(c: Creatura):
    vincitore = "Alieni" if isinstance(c, Alieno) else "Mostri"
    nome = c.getNome()
    testo = f"Ha vinto la fazione dei {vincitore}!\nVincitore: {nome}"
    bordi = "*" * (len(max(testo.splitlines(), key=len)) + 4)
    print(bordi)
    for riga in testo.splitlines():
        print(f"* {riga.ljust(len(bordi) - 4)} *")
    print(bordi)


# Esempio di utilizzo
if __name__ == "__main__":
    alieno = Alieno("Robot-12345")  # nome non corretto, verrà reimpostato
    mostro = Mostro("Godzilla", "", "")  # urlo e gemito non validi, verranno reimpostati

    vincitore = combattimento(alieno, mostro)
    if vincitore:
        proclamaVincitore(vincitore)