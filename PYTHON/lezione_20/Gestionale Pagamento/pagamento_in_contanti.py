from pagamento import Pagamento


class PagamentoContanti (Pagamento):

    def __init__(self,importo):
        super().__init__(importo)

    def dettagliPagamento(self):

        print(f"Importo del pagamento in contanti : €{self.getImporto():.2f}")


    def inPezziDa(self):

        tagli = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 1]
        importo = self.getImporto()
        tagli_utilizzati = []

        importo_cent = round(importo * 100)
   

        for taglio in tagli:
            
            if importo_cent >= taglio:
                quantita = importo_cent // taglio 
                importo_cent -= quantita * taglio
                tagli_utilizzati.extend([taglio / 100] * quantita)

        return tagli_utilizzati






