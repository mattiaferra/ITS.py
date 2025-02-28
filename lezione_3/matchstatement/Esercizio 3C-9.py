lista_cordinate = []
    
cordinata_x= int(input("inserire le cordinate X :  "))
cordinata_y= int(input("inserire le cordinate Y :  "))

lista_cordinate.append(cordinata_x)
lista_cordinate.append(cordinata_y)

tupla_cordinate = tuple(lista_cordinate)

print(tupla_cordinate)

match tupla_cordinate:

    case (0,0):

        print("il punto si trova nell' origine")

    case (x,y) if y == 0:

        print("Il punto si trova sull'asse X.")

    case (x,y) if x == 0:

        print("Il punto si trova sull'asse Y.")

    case (x, y) if x > 0 and y > 0:

        print("Il punto si trova nel primo quadrante")

    case (x, y) if x < 0 and y > 0:

        print("Il punto si trova nel secondo quadrante")

    case (x, y) if x < 0 and y < 0:

        print("Il punto si trova nel terzo quadrante")

    case (x, y) if x > 0 and y < 0:

        print("Il punto si trova nel quarto quadrante")


