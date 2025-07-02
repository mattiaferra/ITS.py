

'''
giorno:int = int(input("inserisci il giorno  (in espressione numerica) : "))

mese:int = int(input("inserisci il mese  (in espressione numerica) : "))
                  

festa:tuple = (giorno, mese)
print(festa)
'''

festa:tuple = (int(input("inserisci il giorno  (in espressione numerica) : ")), int(input("inserisci il mese  (in espressione numerica) : ")) )

print(festa)
print("-----------------------------------------------------")

match festa:

    case (1,1):

        print("la data che hai inserito corrisponde a 'CAPODANNO' ")

    case (14,2):

        print("la data che hai inserito corrisponde a 'SAN VALENTINO' ")

    case (x,6):

        print("la data che hai inserito corrisponde a 'FESTA DELLA REPUBBLICA ITALIANA' ")

    case (15,8):

        print("la data che hai inserito corrisponde a 'FERRAGOSTO' ")

    case (31,10):

        print("la data che hai inserito corrisponde a 'HALLOWEEN' ")

    case (25,12):

        print("la data che hai inserito corrisponde a 'NATALE' ")

    case _:

        print("la data che hai inserito corrisponde a 'NESSUN EVENTO IN PARTICOLARE IN QUESTA DATA' ")




