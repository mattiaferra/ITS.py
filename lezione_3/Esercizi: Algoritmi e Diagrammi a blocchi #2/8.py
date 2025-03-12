A = int(input("inserisci A : "))
B = int(input("inserisci B : "))

somma = 0



if A >= B :

    print("A deve essere minore di B")

elif A < 0 and B < 0 :

    print("A e B devono essere positivi")

elif A % 1 != 0 and B % 1 != 0 :

    print("A e B devono essere interi")

else:

    i = A
    
    for i in range(A,B):

    
        somma = somma + i
        i = i + 1
        
    print(f"la somma dei numeri compresi tra {A} e {B} è : {somma}")