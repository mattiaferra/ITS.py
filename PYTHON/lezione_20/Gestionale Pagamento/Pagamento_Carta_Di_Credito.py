from pagamento import Pagamento

class PagamentoCartaDiCredito(Pagamento):

    def __init__(self, importo: float, titolare: str, scadenza: str, numero: str):
        super().__init__(importo)
        self.titolare = titolare
        self.scadenza = scadenza
        self.numero = numero

    def dettagliPagamento(self):

        return (
            f"Importo del pagamento: €{self.getImporto():.2f} pagato con Carta di Credito\n"
            f"Dettagli:\n"
            f"Nome del titolare della carta: {self.titolare}\n"
            f"Data di scadenza: {self.scadenza}\n"
            f"Numero carta che termina con : **** **** **** {self.numero[-4:]}"
        )
