class Media:
    def __init__(self,title : str ):

        self.title = title
        self.reviews = []




    def set_title(self, titolo):

        self.title = titolo


    def get_title(self):

        return self.title
    


    def aggiungiValutazione(self, voto): #Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).

        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)


    def getMedia(self): #Calcola e restituisce la media delle valutazioni.


        if not self.reviews:
            return 0 # Evita divisione per zero se non ci sono valutazioni


        somma = 0

        for i in self.reviews:

            somma+=i

        media = somma/len(self.reviews)
        return media
    


    def getRate(self): #Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.

        media = self.getMedia()

        if media < 1.5: 
            return "Terribile"
        
        elif media < 2.5:
            return "Brutto"
        
        elif media < 3.5:
            return "Normale"
        
        elif media < 4.5:
            return "Bello"
        
        else:
            return "Grandioso"
        

    def ratePercentage(self, voto): #Calcola e restituisce la percentuale di un voto specifico nelle recensioni.

       percentuale = ( self.reviews.count(voto) / len(self.reviews) ) * 100

       return percentuale
    

    def recensione(self): 

        print(f"Titolo del Film: {self.get_title()}")
        media = self.getMedia()
        print(f"Voto Medio: {media:.2f}")
        print(f"Giudizio: {self.getRate()}")
        