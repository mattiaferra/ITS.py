n = float(input("inserisci n : "))

if n < 0 :

    print("deve essere positivo")

if n % 1 != 0 :

    print("deve essere intero positivo")

cont = 0 
i = 0


while i < 10 : 

    x = int(input("inserisci x : "))


    if x % n == 0 :

        cont = cont + 1
    i = i + 1

print(f"sono divisibili per {n:.0f}, {cont} numeri")



    


