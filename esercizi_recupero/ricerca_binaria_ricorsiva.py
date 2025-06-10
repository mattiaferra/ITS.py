def bin_search(lista:list, num : int)-> None:

    mid : int = len(lista)//2

    if lista[mid] == num:

        print(f"Numero trovato in posizione {mid}")

    elif len(lista[mid]) == 1:

        print("Numero non trovato")


    elif lista[mid] > num :

        bin_search(lista[:mid], num) 


    elif lista[mid] < num:

        bin_search(lista[mid + 1:], num)


    def bin_search_iterative(lista,num):

        i , j = 0, len(lista) -1

        while True:

            mid = len(lista[i: j])//2  # i = inizio j = fine | conclusione dall'inizio alla fine

            if lista[mid] == num:

                print("Ho trovato il numero")

            elif num < lista[mid]:
                
                j = mid

            elif num > lista[mid]:

                i = mid + 1 
            



    