class Documento : 
    def __init__(self,testo : str):
        
        self.testo = testo



    def getText(self) :

        return self.testo
    


    def  setText(self,text): 

        self.testo = text     



    def  isInText(self,parola):

        if parola in self.testo : 

            return True
        



class Email(Documento):

    def __init__(self, testo, mittente, destinatario, oggetto):
        super().__init__(testo)

        self.mittente = mittente
        self.destinatario = destinatario
        self.oggetto = oggetto
        self.corpo = testo


    def  getMittente(self):

            return self.mittente
    
    def setMittente(self,m):

        self.mittente = m


    def getDestinatario(self):

        return self.destinatario
    
    def setDestinatario(self,d):

        self.destinatario = d


    def getOggetto(self):

        return self.oggetto 
    
    def setOggetto(self,o):

        self.oggetto = o



    def getText(self):

        return f"Da: {self.mittente},  A: {self.destinatario}\nOggetto: {self.oggetto}\nCorpo: {self.corpo}"
    

    def writeToFile(self,percosoFile): 

        with open(percosoFile,'w') as file:
            
            file.write(self.getText())




class File(Documento):
    def __init__(self, nomePercorso):
        self.nomePercorso = nomePercorso
        self.testo = ""

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
            self.testo = file.read()

    def getText(self):
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"




doc = Documento(testo="CIAOOO")
test = Email(testo=doc.getText(), mittente="Mattia", destinatario="Luigi", oggetto="Saluto")
test_parola_chiave = test.isInText("CIAOOO")

print(test.getText())
print(test_parola_chiave)


# Esempio di utilizzo

# Creazione e salvataggio di un'email
email = Email(
    testo="Ciao Bob, possiamo incontrarci domani?",
    mittente="alice@example.com",
    destinatario="bob@example.com",
    oggetto="Incontro"
)
# Assicurati che la cartella 'ES' esista prima di eseguire questa riga
email.writeToFile("ES/email_output.txt")

# Creazione di un file con contenuto testuale
with open("ES/document.txt", "w") as f:
    f.write("Questo e' il contenuto del file.")

# Lettura del contenuto da file
file_doc = File("ES/document.txt")
file_doc.leggiTestoDaFile()

# Stampa dei risultati
print(email.getText())
print()
print(file_doc.getText())




