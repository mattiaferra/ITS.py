import math


def calculateCharges(ora_durata_parcheggio : float ):

    if ora_durata_parcheggio <=  3 :

        costo = 2

    elif ora_durata_parcheggio == 24:

        costo = 10

    
    elif ora_durata_parcheggio > 3 and ora_durata_parcheggio < 24:

        costo = 2 + (ora_durata_parcheggio - 3) * 0.50

    return round(costo)



cars = [
    {"car": 1, "hours": 1.5},
    {"car": 2, "hours": 4.0},
    {"car": 3, "hours": 5.5},
    {"car": 4, "hours": 24.0},
]

# Stampa intestazione
print(f"{'Car':<10}{'Hours':<15}{'Charge'}")

# Totali
total_hours = 0
total_charge = 0

# Calcolo e stampa riga per riga
for c in cars:
    charge = calculateCharges(c["hours"])
    total_hours += c["hours"]
    total_charge += charge
    print(f"{c['car']:<10}{c['hours']:<15.2f}{charge:.2f} $")

# Stampa totali
print(f"{'TOTAL':<10}{total_hours:<15.1f}{total_charge:.2f} $")