n = int(input("Inserisci n : "))

i = 0

while i < n :

    x = int(input("Inserisci x : "))
    y = int(input("Inserisci y : "))

    # Se entrambi i numeri sono positivi, calcola il prodotto

    if x > 0 and y > 0:

        result = x * y
        print(f"Il prodotto tra x e y è : {result}")

        i = i + 1
        break

    # Altrimenti controlla se uno è positivo e l'altro negativo (logica XOR)

    else:

        x_negativo = x < 0
        y_negativo = y < 0

        xor = (x_negativo and not y_negativo) or (not x_negativo and y_negativo)
        
        if xor:

            result = x + y
            print(f"La somma tra x e y è : {result}")

            i = i + 1

        else:

            print("Errore!")

            


