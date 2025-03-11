while True:

    n = int(input("Inserisci n: "))

    if n > 0:

        break  
    else:

        print("Il numero inserito deve essere positivo.")

fattoriale = 1 
i = 1

while i <= n:
    
    fattoriale *= i
    i += 1

print(fattoriale)