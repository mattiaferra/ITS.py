
somma_di_tutto = []
somma_testa = []
somma_croce = []

for i in range(8):

    risultato = input(f"Lancio {i+1} : ").lower()

    match risultato:

        case "t":
            somma_di_tutto.append(risultato)
            somma_testa.append(risultato)

        case "c":
            somma_di_tutto.append(risultato)
            somma_croce.append(risultato)

percentuale_testa = (len(somma_testa)/len(somma_di_tutto))*100

percentuale_croce = (len(somma_croce)/len(somma_di_tutto))*100

print("-----------------------------------------")

print(f"Totale testa = {len(somma_testa)}")
print(f"Totale croce = {len(somma_croce)}")

print(f"Percentuale Testa = {percentuale_testa}")
print(f"Percentuale Testa = {percentuale_croce}")



