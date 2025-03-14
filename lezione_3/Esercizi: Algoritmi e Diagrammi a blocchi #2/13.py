x = int(input("inserisci x : "))
y = int(input("inserisci y : "))
z = int(input("inserisci z : "))


if x % 1 == 0 and x < 0 :

    print("x deve essere intero e positivo")


if y % 1 == 0 and y < 0 :

    print("y deve essere intero e positivo")


if z % 1 == 0 and z < 0 :

    print("z deve essere intero e positivo")


else : 

    if (x + y + z)% 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0 :

        print("regole rispettate")


    else:

        print("regole non rispettate")