class Pagamento:
    def __init__(self):
        
        self.__importo = 0.0


    def setImporto(self, importo : float):

        self.__importo = importo


    def getImporto(self):   

        return self.__importo
    

    def dettagliPagamento(self):

        print(f"Importo del pagamento: €{self.__importo:.2f}")

