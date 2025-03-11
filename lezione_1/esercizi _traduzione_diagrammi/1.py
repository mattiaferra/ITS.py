import math

cateto_a = int(input("inserisci la misura del cateto a : "))
cateto_b = int(input("inserisci la misura del cateto b : "))


if cateto_a > cateto_b:

    cateto_c = math.sqrt(cateto_a**2-cateto_b**2)
    print(cateto_c)

else:

    print("errore!")


